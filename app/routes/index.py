import os

from flask import Blueprint, jsonify
from pymongo import MongoClient

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def welcome():
    return "Welcome to the Task Management App!"


@index_bp.route("/check-mongo")
def check_mongo_connection():
    try:
        mongo_uri = os.getenv("MONGO_URI")
        client = MongoClient(mongo_uri)
        db_names = client.list_database_names()
        return jsonify({"message": "Connected to MongoDB", "databases": db_names}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
