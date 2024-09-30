import sys
from os.path import abspath, dirname

import pytest
from pymongo import MongoClient

from app import create_app
from app.models.user import User

sys.path.insert(0, abspath(dirname(dirname(__file__))))


def test_user_model_creation(client):
    user = User(
        username="testuser", email="testuser@example.com", password="testpassword"
    )
    user_id = user.save_to_db()

    # Retrieve user data from the database
    inserted_user = User.find_by_email("testuser@example.com")

    assert inserted_user is not None
    assert inserted_user["username"] == "testuser"
    assert inserted_user["email"] == "testuser@example.com"
