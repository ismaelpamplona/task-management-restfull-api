import re

import bcrypt
from flask import Blueprint, jsonify, request

from app.models.user import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()

    if (
        not data
        or not data.get("username")
        or not data.get("email")
        or not data.get("password")
    ):
        return jsonify({"error": "Invalid input"}), 400

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, data["email"]):
        return jsonify({"error": "Invalid email format"}), 400

    if len(data["password"]) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    user = User(
        username=data["username"], email=data["email"], password=data["password"]
    )

    user_id = user.save_to_db()

    return (
        jsonify(
            {
                "message": "User registered successfully",
                "user": {
                    "id": str(user_id),
                    "username": user.username,
                    "email": user.email,
                },
            }
        ),
        201,
    )


@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Invalid input"}), 400

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, data["email"]):
        return jsonify({"error": "Invalid email format"}), 400

    user = User.find_by_email(data["email"])

    if user is None or not bcrypt.checkpw(
        data["password"].encode("utf-8"), user["password"].encode("utf-8")
    ):
        return jsonify({"error": "Invalid email or password"}), 401

    return (
        jsonify(
            {
                "message": "Login successful",
                "access_token": "mocked_token",  # replace later
            }
        ),
        200,
    )
