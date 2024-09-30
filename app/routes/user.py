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
