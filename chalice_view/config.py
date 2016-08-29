import os
import json


class Config(object):
    __base_dir = os.path.dirname(os.path.abspath(__file__))
    __cwd = os.getcwd()
    __default_config_path = os.path.join(__cwd, '.chalice', 'config.json')

    def __init__(self, config_path=None):
        if not config_path:
            config_path = self.__default_config_path
        with open(config_path, 'rb') as f:
            self.config = json.loads(f.read())

    @property
    def app_name(self):
        return self.config['app_name']

    @property
    def debug(self):
        return self.config.get('stage', '') == 'dev'
