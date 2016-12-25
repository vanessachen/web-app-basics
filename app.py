# -*- coding: utf-8 -*-

'''
   quizapp
   written by @enrobyn

   Flask application for learning new things.
   Enables a user to check their progress on a memorization task.
   Designed to be used to teach full stack web dev.
   Debugging should be turned off for deployment but this code
   may be used for testing on a local machine.
'''

import arrow
from bson import ObjectId
from datamodels import db, scorecards, thingstolearn, users
from flask import (
    Flask, g, session, flash, render_template, 
    request, url_for, redirect, jsonify
)
from forms import LoginForm, SignupForm, WordForm
from functools import wraps
import json
import math, random
from passlib.hash import pbkdf2_sha512
from pymongo import MongoClient, errors
import secure
from uuid import uuid4


app = Flask(__name__)
app.debug = True
app.secret_key = secure.APP_SECRET_KEY # TODO change for production


@app.before_request
def before_request():
    '''
    If there is a user currently in the session, look up their information in
    the database and set `g.user`.
    '''

    g.user = None
    if "user" in session:
        g.user = db.users.find_one({"uuid":session["user"]})

def is_admin():
    return g.user and g.user["role"] == "admin"

def is_admin_visible():
    return g.user and g.user["role"] in ["admin", "moderator"]

def is_logged_in():
    return bool(g.user)

@app.context_processor              # TODO: comment this code
def add_utils_to_template_context():
    return dict(
        is_admin_visible=is_admin_visible,
        is_logged_in=is_logged_in,
    )

def login_required(f):
    '''
    View decorator that ensures a logged-in user is in the session, redirecting
    to the login page otherwise.
    '''
    @wraps(f)
    def inner(*a, **kw):
        if not is_logged_in():
            return redirect(url_for("login"))
        return f(*a, **kw)
    return inner


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():     
    '''
    A route which serves a word quiz feature, displaying a definition and
    prompting the user to type the word described by that definition.
    '''
    wform = WordForm()
    session["subtopic"] = "mongodb"  # TODO: auto-generate this

    if request.method == "GET":
        cursor          = db.thingstolearn.aggregate(  [ { "$sample": { "size": 1 } } ])
        random_doc      = cursor.next()
        definition      = random_doc["definition"]
        answer          = random_doc["word"]
        session["item"] = answer # store the right answer on the session object
        session["start_time"] = arrow.utcnow().timestamp # start the timer
        return render_template("quiz.html", definition=definition, wform=wform)

    if request.form["submit"] == "guess" and wform.validate_on_submit():
        stop_time       = arrow.utcnow().timestamp # stop the timer
        tot_time        = stop_time - session["start_time"]
        guess           = wform.word_guess.data    # retrieve the user's guess from the form
        correct         = (guess == session["item"]) # check if the answer is right
        # get this user's scores from the scorecards collection
        all_scores      = db.scorecards.find_one(
                            {"uuid": session["user"], "start_time": session["session_start"]},
                            )
        if all_scores == None: # the session just started; this is the first quiz prob
            all_scores = {
                "uuid": session["user"],
                "start_time": session["session_start"],
                "subtopic": session["subtopic"]
            }

        if session["item"] in all_scores: # if they've seen this item before
            this_word   = all_scores[session["item"]] # scorecard for this particular word
        else: # this is the first time user has seen this during this session
            this_word   = {
                "attempts"  : 0,
                "num_right" : 0,
                "time_spent"  : 0
            }
        this_word["attempts"] += 1
        this_word["num_right"] += (1 if correct else 0)
        this_word["time_spent"] += tot_time 

        # using an upsert operation, 
        # put the info into the "scorecards" database
        db.scorecards.find_one_and_update(
            {"uuid": session["user"], "start_time": session["session_start"]}, 
            {"$set": { session["item"] : this_word}},
            upsert=True)

        return redirect(url_for("quiz"))

    return render_template("quiz.html", definition=definition, wform=wform)
 
@app.route("/logout", methods=["GET"])
def logout():
    if "user" in session:
        del session["user"]
    return "thanks for using this app !" #redirect(url_for('index'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if g.user: 
        session["session_start"] = arrow.utcnow().timestamp
        return redirect(url_for("quiz"))

    rform = SignupForm()    # "R" stands for Register
    lform = LoginForm()     # "L" stands for Login
    if request.method == "GET":
        return render_template("login.html", rform=rform, lform=lform)

    user = None             # "user" will be used to store a dict for this user

    if request.form["submit"] == "reg" and rform.validate_on_submit():
        # TODO: ensure valid email address
        fname       = rform.fname.data
        lname       = rform.lname.data
        username    = rform.username.data
        email       = rform.email.data
        password    = rform.password.data
        hashed      = pbkdf2_sha512.encrypt(password)

        new_user    = {
            "first_name": fname,
            "last_name": lname,
            "username": username,
            "uuid": str(uuid4().urn),
            "email": email,
            "password_hash": hashed,
            "cohort": "webdev",
            "date_created": arrow.utcnow().timestamp,
            "last_login": arrow.utcnow().timestamp,
            "role": "root",
            "courses": []               
        }

        try:
            db.users.insert_one(new_user)
        except DuplicateKeyError as e: # there is an index on "username"
            flash("username already in use")
            return render_template("login.html", rform=rform, lform=lform)
        
        user = new_user
        new_user = None


    elif request.form["submit"] == "login" and lform.validate_on_submit():
        print("Attempting to validate...")
        uname       = lform.uname.data
        print("they typed {}".format(uname))
        passphrase  = lform.passphrase.data
        print("AND the pwd had {} chars".format(len(passphrase)))
        if (db.users.find({"username":uname}).count() > 0):
            print("a user was FOUND")
            someuser = db.users.find_one({"username":uname})
            the_hash = someuser["password_hash"] # the right answer
            if pbkdf2_sha512.verify(passphrase, the_hash):
                print("hash match!!!!!!")
                user = someuser                  

    if user:
        session["user"] = user["uuid"]
        session["session_start"] = arrow.utcnow().timestamp
        return redirect(url_for("quiz"))

    return render_template("login.html", rform=rform, lform=lform)


@app.route("/api/testdata", methods=["GET"])
@login_required
def testdata():
    ''' A route which enables a logged-in user to access raw data
        from the current session in JSON format.
    '''
    # get the scorecard from this session
    session_scores      = db.scorecards.find_one(
                            {"uuid": session["user"], "start_time": session["session_start"]},
                            )
    if session_scores == None:
        return "No session data to display"
    else:
        clean_data = [] # empty list in which to accumulate session scores
        # get a cursor of all the things from this subtopic
        could_have_learned = db.thingstolearn.find({"subtopic": session["subtopic"]})
        length = could_have_learned.count()
        for i in range(0, length):
            thing = could_have_learned.next()["word"]
            if thing in session_scores: # if the user was tested on this item
                item_scores = {
                    "item_name": thing,
                    "topic_area": session["subtopic"],
                    "session_data": session_scores[thing] # retrieve the session scores
                }
                clean_data.append(item_scores)
        return (json.dumps(clean_data, indent=4, separators=(",", ": ")), "200 OK", {"Content-type": "application/json"})

if __name__ == "__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["DEBUG"] = True # TODO change for production
    ''' next line: cause KeyErrors to bubble up to top level 
    so we can see the traceback & debugger '''
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run()
