import json


def get_config(custom_config_filename: str, default_config: dict):
    with open(custom_config_filename) as file_handler:
        file_content = file_handler.read().replace("\r", "").replace("\n", "")
        custom_config_dict = json.loads(file_content)
        for key, value in custom_config_dict.items():
            default_config[key] = value
    return default_config


class Config:
    def __init__(self, config: dict):
        self.config = config

    def get_eps(self):
        return self.config["eps"]
