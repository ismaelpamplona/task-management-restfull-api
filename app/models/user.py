import os

import bcrypt
from pymongo import MongoClient


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def save_to_db(self):
        mongo_uri = os.getenv("MONGO_URI")
        client = MongoClient(mongo_uri)
        db = client.get_database("task_management")
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        result = db.users.insert_one(user_data)
        client.close()
        return result.inserted_id

    @staticmethod
    def find_by_email(email):
        mongo_uri = os.getenv("MONGO_URI")
        client = MongoClient(mongo_uri)
        db = client.get_database("task_management")
        user = db.users.find_one({"email": email})

        client.close()
        return user
