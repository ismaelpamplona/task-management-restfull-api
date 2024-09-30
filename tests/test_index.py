import sys
from os.path import abspath, dirname

import pytest

from app import create_app

sys.path.insert(0, abspath(dirname(dirname(__file__))))


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_welcome_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to the Task Management App!"
