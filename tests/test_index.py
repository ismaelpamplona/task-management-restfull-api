import sys
from os.path import abspath, dirname

import pytest

from app import create_app

sys.path.insert(0, abspath(dirname(dirname(__file__))))


def test_welcome_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to the Task Management App!"
