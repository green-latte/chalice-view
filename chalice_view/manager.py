from .app import App
from .config import Config
from .utils import req2levent
import exceptions as exp


class AppManager(object):
    def __init__(self):
        config = Config()
        self.__app = App(app_name=config.app_name, debug=config.debug)

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
        return self.__app.chalice_app


__all__ = ['AppManager']
