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

@app.route("/progress", methods=["GET"])
def progress():
    render_template("progress.html")
   

if __name__ == "__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["DEBUG"] = True # TODO change for production
    ''' next line: cause KeyErrors to bubble up to top level 
    so we can see the traceback & debugger '''
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run()
