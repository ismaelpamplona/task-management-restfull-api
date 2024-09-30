from flask import Flask

from app.routes.index import index_bp
from config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(index_bp)

    return app
