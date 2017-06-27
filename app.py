# -*- coding: utf-8 -*-

'''
   sample code to learn Flask

   From the terminal, run: 

        $ python app.py

    and then, in a browser, go to:

        http://127.0.0.1:5000/progress

   Debugging should be turned off for deployment but this code
   may be used for testing on a local machine.
'''

import arrow
from flask import (
    Flask, g, session, flash, render_template, 
    request, url_for, redirect, jsonify
)
from functools import wraps
import json
import math, random

# this is a hard-coded example for demo purposes
APP_SECRET_KEY = "this is a secret" # change for production

app = Flask(__name__)
app.debug = True
app.secret_key = APP_SECRET_KEY # hard-coded for demo



# this code creates a ROUTE.
# A route is connected to a URL.


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the app!"


@app.route("/demo", methods=["GET"])
def demo():
    list_name = "Day 1 Vocabulary"

    needs_work = ["git init", "pip", "asynchronous"]

    return render_template("demo.html", list_name=list_name, needs_work=needs_work)
   

@app.route("/progress", methods=["GET"])
def progress():
    # here is a Python variable named `the_message`
    the_message = "Hello! This is the progress page!"

    # Look carefully at the items in parentheses here:
    return render_template("progress.html", the_message=the_message)
   

# Don't worry about the code below this line -- 
# this is some fancy stuff which enables us to 
# view error messages in the browser.

if __name__ == "__main__":
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["DEBUG"] = True # TODO change for production
    ''' next line: cause KeyErrors to bubble up to top level 
    so we can see the traceback & debugger '''
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run()
