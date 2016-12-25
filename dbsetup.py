'''
	Database setup for the quiz app
	ONLY NEED TO RUN THIS FILE ONCE
'''

import arrow
from pymongo import MongoClient, ASCENDING
from secure import MONGO_USERNAME, MONGO_PASSWORD
from passlib.hash import pbkdf2_sha512
from uuid import uuid4


# SET UP THE CONNECTION

client 		= MongoClient("localhost", 27017)
db 		= client["aprender"]  # database
thingstolearn 	= client["thingstolearn"]  # collection
users 		= client["users"]  # collection
client.aprender.authenticate(MONGO_USERNAME, MONGO_PASSWORD, mechanism='SCRAM-SHA-1')

print("using db {}".format(db.name))
print("using collection {}".format(db.thingstolearn.name))

someword = db.thingstolearn.find_one()
print(someword)
print("a word is {}".format(someword["word"]))

first_user = {
        "first_name": "",
        "last_name": "",
        "username": "someusername",
        "uuid": str(uuid4().urn),
        "email": "emailaddress",
        "password_hash": "", # put a hash here!!!
        "cohort": "quizapp",
        "date_created": arrow.utcnow().timestamp,
        "last_login": arrow.utcnow().timestamp,
        "role": "user",
        "courses": []
}	

db.users.insert_one(first_user)
print(db.users.find_one())

# MAKE AN INDEX ON THE "USERNAME" KEY
db.users.create_index([("username", ASCENDING)], unique=True)
# TODO uncomment for production
# MAKE AN INDEX ON THE "TOPIC" KEY
#db.thingstolearn.create_index([("topic", ASCENDING)], unique=True)
