import os.path

from src.config import get_config
from src.config import Config


def get_eps():
    default_config = {}
    config_file = os.path.join(os.path.dirname(__file__), "..", "config", "main.json")
    return Config(get_config(config_file, default_config)).get_eps()


def approximately_equal(value: float, expected_value: float):
    if value is None or expected_value is None:
        if value is None and expected_value is None:
            return True
        else:
            return False
    return approximately_equal_with_eps(value, expected_value, get_eps())


def approximately_equal_with_eps(value: float, expected_value: float, eps: float):
    if abs(value - expected_value) < eps:
        return True
    return False
