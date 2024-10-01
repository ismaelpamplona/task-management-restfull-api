from flask import Flask
from flask_jwt_extended import JWTManager

from app.routes import index_bp, user_bp
from config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt = JWTManager(app)
    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)

    return app
