import importlib

from .app import App, AppModule
from .cli import cli
from .config import Config
from .utils import req2levent
import exceptions as exp


class AppManager(object):
    app_modules = []

    def __init__(self, settings=None):
        if not settings:
            raise exp.InvalidChaliceSetting('Invalid Chalice Config')
        config = Config(settings)
        self.__app = App(app_name=config.app_name, debug=config.debug)
        self.__config = config
        self.analyze_applications()

    def analyze_applications(self):
        custom_apps = self.__config.app_modules
        for app in custom_apps:
            mod = AppModule(app)
            self.app_modules.append(mod)

    def register(self, path, view_cls):
        self.__app.router.register(path, view_cls)

    def as_view(self):
        def call_view(request):
            event, context = req2levent(self.__app.chalice_app, request)
            response = self.__app.chalice_app.__call__(event, context)
            if not isinstance(response, dict):
                raise exp.BadResponseError("Unsupported response: %s" % type(response))
            return response
        return call_view

    def generate_app(self):
        # dispatch routes
        self.dispatch_routes()
        return self.__app.chalice_app

    def dispatch_routes(self):
        for mod in self.app_modules:
            routers = mod.routers
            for r in routers:
                self.register(r.path, r.view_cls)

    def cli(self):
        return cli(obj={'manager': self})


__all__ = ['AppManager']
