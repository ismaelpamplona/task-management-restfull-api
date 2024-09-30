import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(dirname(__file__))))

from config.config import Config


def test_config_loading() -> None:
    assert Config.FLASK_ENV == "development"
    assert (
        Config.MONGO_URI
        == "mongodb://root:example@mongo:27017/task_management?authSource=admin"
    )
