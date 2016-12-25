# quizapp
a Word Quiz flask app 

Notes for the Quiz App

The purpose of this app is to teach full stack web development.  quizapp is a Flask application (written in Python 3) which demonstrates the use of MongoDB with pymongo.  In order to run this code on your local machine, follow these steps:

1. clone the repo

2. set up a virtual environment

virtualenv -p python3 qenv

3. start the virtualenv

. qenv/bin/activate

4. upgrade pip immediately to avoid installation errors

pip install --upgrade pip

5. install required packages:

pip install -r requirements.txt

6. in a new terminal window, start a MongoDB instance

mongod

7. import the example data!
(edit this command to include the proper filepath)

mongoimport --db aprender --collection thingstolearn --type csv --headerline --file /file/path/to/the/CSV/quizwords.csv

8. run the db setup file (ONLY ONCE)

python dbsetup.py

9. run the app

python app.py

If successful, you should then see a message such as:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: (numbers)

10. using a browser, go to the following address:

http://127.0.0.1:5000/login
