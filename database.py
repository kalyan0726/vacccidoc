import pymongo
from pymongo import MongoClient
import pytz
import bcrypt

cluster = MongoClient("mongodb+srv://kalyan0726:kalyan0726@cluster0.fux9x.mongodb.net/myFirstDatabase?retryWrites=true")
db = cluster["vaccidoc"]
collection = db["login_info"]


def create_profile_db(profile):
    password = profile["pw"]
    en_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    profile["pw"] = en_pw
    if collection.find_one({"user_email": profile["user_email"]}) is not None:
        return False
    else:
        collection.insert_one(profile)
        return True


def verify_user(Email, password):
    # verify user credentials and authenticate user.
    profile = collection.find_one({"user_email": Email})
    if profile == None:
        return False
    else:
        Stored_hashedpw = profile["pw"]
        Given_hashedpw = bcrypt.hashpw(password.encode('utf8'), Stored_hashedpw)

        if Given_hashedpw == Stored_hashedpw:
            return True
        else:
            return False




