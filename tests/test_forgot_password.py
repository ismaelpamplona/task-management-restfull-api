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
