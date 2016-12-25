'''
	Database client setup for the "aprender" app
'''

# TODO enable auth
# https://docs.mongodb.com/v3.2/tutorial/enable-authentication/

import arrow
from passlib.hash import pbkdf2_sha512
from pymongo import MongoClient
from secure import MONGO_USERNAME, MONGO_PASSWORD
from uuid import uuid4

# SET UP THE CONNECTION

client 			= MongoClient("localhost", 27017)
db 				= client["aprender"] 
scorecards		= client["scorecards"]
thingstolearn 	= client["thingstolearn"] 
users 			= client["users"]

# AUTHENTICATE THE CONNECTION

client.aprender.authenticate(MONGO_USERNAME, MONGO_PASSWORD, mechanism='SCRAM-SHA-1')

'''

print("using db {}".format(db.name))
print("using collection {}".format(db.thingstolearn.name))

someword = db.thingstolearn.find_one()
print(someword)
print("a word is {}".format(someword["word"]))

'''

