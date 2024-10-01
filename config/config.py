import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="dev.env")


class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
