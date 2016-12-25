# quizapp
a Word Quiz flask app 

##Notes for the Quiz App

The purpose of this app is to teach full stack web development.  quizapp is a Flask application (written in Python 3) which demonstrates the use of MongoDB with pymongo.  In order to run this code on your local machine, follow these steps:

* clone the repo

* set up a virtual environment

`virtualenv -p python3 qenv`

* start the virtualenv

`. qenv/bin/activate`

* upgrade pip immediately to avoid installation errors

`pip install --upgrade pip`

* install required packages:

`pip install -r requirements.txt`

* in a new terminal window, start a MongoDB instance

`mongod`

* import the example data!
(edit this command to include the proper filepath)

`mongoimport --db aprender --collection thingstolearn --type csv --headerline --file /file/path/to/the/CSV/quizwords.csv`

* run the db setup file (ONLY ONCE)

`python dbsetup.py`

* run the app

`python app.py`

If successful, you should then see a message such as:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: (numbers)
```

10. using a browser, go to the following address:

http://127.0.0.1:5000/login
