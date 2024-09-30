import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(dirname(__file__))))

import pytest
from pymongo import MongoClient

from app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

    # Cleanup: Connect to MongoDB and clear the test database
    mongo_uri = app.config["MONGO_URI"]
    client_mongo = MongoClient(mongo_uri)
    db = client_mongo.get_database("task_management_test")
    db.users.delete_many({})
    client_mongo.close()
