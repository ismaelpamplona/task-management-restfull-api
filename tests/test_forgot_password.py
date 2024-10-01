def test_request_password_reset(client):
    # First, register a user
    client.post(
        "/register",
        json={
            "username": "forgotuser",
            "email": "forgotuser@example.com",
            "password": "forgotpassword",
        },
    )

    # Request a password reset for the registered user
    response = client.post(
        "/forgot-password",
        json={"email": "forgotuser@example.com"},
    )

    assert response.status_code == 200
    assert response.json["message"] == "Password reset link sent to your email"

    # Request password reset for a non-existent user
    response = client.post(
        "/forgot-password",
        json={"email": "nonexistent@example.com"},
    )

    assert response.status_code == 404
    assert response.json["error"] == "Email not found"


def test_password_reset_token_generation(client):
    # Register a user to test password reset
    client.post(
        "/register",
        json={
            "username": "tokenuser",
            "email": "tokenuser@example.com",
            "password": "tokenpassword",
        },
    )

    # Request a password reset
    response = client.post(
        "/forgot-password",
        json={"email": "tokenuser@example.com"},
    )

    assert response.status_code == 200
    assert "reset_token" in response.json
    assert response.json["message"] == "Password reset link sent to your email"
    # Check that the token is not empty
    assert response.json["reset_token"] != ""
