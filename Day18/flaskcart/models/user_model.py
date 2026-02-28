from utils.db import db

users = db.users

def create_user(data):
    return users.insert_one(data)

def find_user_by_email(email):
    return users.find_one({"email": email})

def find_user_by_id(user_id):
    return users.find_one({"_id": user_id})