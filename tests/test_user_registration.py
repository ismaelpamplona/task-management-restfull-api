import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_user_registration(client):
    response = client.post(
        "/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        },
    )

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
