import os
import json

import exceptions as exp


class Config(object):
    __base_dir = os.path.dirname(os.path.abspath(__file__))
    __cwd = os.getcwd()
    __default_config_path = os.path.join(__cwd, '.chalice', 'config.json')

    def __init__(self, settings):
        self.settings = settings
        # find default chalice config dir
        config_path = getattr(settings, 'CHALICE_CONFIG_DIR')
        if not config_path:
            config_path = self.__default_config_path
        else:
            config_path = os.path.join(config_path, 'config.json')
        # load .chalice/config.json
        with open(config_path, 'rb') as f:
            self.config = json.loads(f.read())

    @property
    def app_name(self):
        # get app name from settings.py or .chalice/config.json
        return getattr(self.settings, 'APPLICATION_NAME') or self.config['app_name']

    @property
    def debug(self):
        return getattr(self.settings, 'DEBUG') or False

    @property
    def app_modules(self):
        apps = getattr(self.settings, 'APPLICATIONS')
        if not isinstance(apps, tuple):
            raise exp.ApplicatonLoadingError('Set app name in list or tuple')
        return apps
