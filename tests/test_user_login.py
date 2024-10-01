import bcrypt
import pytest
from pymongo import MongoClient

from app import create_app
from app.models.user import User


def test_user_login(client):
    client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
        },
    )

    response = client.post(
        "/login",
        json={
            "email": "testuser@example.com",
            "password": "testpassword",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json
    assert response.json["message"] == "Login successful"
