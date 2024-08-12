import json


class ConfigProvider:

    @staticmethod
    def load_config_json(file):
        try:
            with open(file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"file {file} not found")