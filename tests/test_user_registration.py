import bcrypt
import pytest
from pymongo import MongoClient

from app import create_app
from app.models.user import User


def test_user_registration(client):
    response = client.post(
        "/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        },
    )

    user = User.find_by_email("newuser@example.com")

    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"
    assert response.json["user"]["username"] == "newuser"
    assert response.json["user"]["email"] == "newuser@example.com"


def test_user_registration_invalid_input(client):
    # Test missing email
    response = client.post(
        "/register", json={"username": "user", "password": "password"}
    )
    assert response.status_code == 400
    assert response.json["error"] == "Invalid input"

    # Test invalid email format
    response = client.post(
        "/register",
        json={"username": "user", "email": "invalid-email", "password": "password"},
    )
    assert response.status_code == 400
    assert response.json["error"] == "Invalid email format"

    # Test short password
    response = client.post(
        "/register",
        json={"username": "user", "email": "user@example.com", "password": "123"},
    )
    assert response.status_code == 400
    assert response.json["error"] == "Password must be at least 6 characters long"


def test_password_is_hashed():
    user = User(username="test", email="test@example.com", password="plainpassword")
    user.save_to_db()

    # Retrieve the inserted user
    inserted_user = User.find_by_email("test@example.com")

    assert inserted_user is not None
    # Check that the password is not stored in plain text
    assert inserted_user["password"] != "plainpassword"
    # Check that the hashed password matches the original password using bcrypt
    assert bcrypt.checkpw(
        "plainpassword".encode("utf-8"), inserted_user["password"].encode("utf-8")
    )


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
