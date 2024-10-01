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


def test_user_login_invalid_input(client):
    # Test missing email
    response = client.post("/login", json={"password": "testpassword"})
    assert response.status_code == 400
    assert response.json["error"] == "Invalid input"

    # Test invalid email format
    response = client.post(
        "/login", json={"email": "invalid-email", "password": "testpassword"}
    )
    assert response.status_code == 400
    assert response.json["error"] == "Invalid email format"

    # Test missing password
    response = client.post("/login", json={"email": "testuser@example.com"})
    assert response.status_code == 400
    assert response.json["error"] == "Invalid input"


def test_user_login_incorrect_credentials(client):
    # First, register a user to test login functionality
    client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
        },
    )

    # Try logging in with an incorrect password
    response = client.post(
        "/login",
        json={"email": "testuser@example.com", "password": "wrongpassword"},
    )

    assert response.status_code == 401
    assert response.json["error"] == "Invalid email or password"

    # Try logging in with an unregistered email
    response = client.post(
        "/login",
        json={"email": "unregistered@example.com", "password": "testpassword"},
    )

    assert response.status_code == 401
    assert response.json["error"] == "Invalid email or password"


def test_user_login_jwt_token(client):
    # First, register a user
    client.post(
        "/register",
        json={
            "username": "jwtuser",
            "email": "jwtuser@example.com",
            "password": "jwtpassword",
        },
    )

    # Now, attempt to log in
    response = client.post(
        "/login",
        json={"email": "jwtuser@example.com", "password": "jwtpassword"},
    )

    assert response.status_code == 200
    assert "access_token" in response.json
    assert response.json["message"] == "Login successful"
    # Verify that the token is not empty
    assert response.json["access_token"] != "mocked_token"
