import inspect
import importlib
import unittest
from chalice import Chalice

from .routes import BaseRouter


class App(object):
    __config = None

    def __init__(self, app_name='', debug=False):
        self.__app = Chalice(app_name=app_name)
        self.__app.debug = debug
        self.__router = BaseRouter(self.__app)

    @property
    def router(self):
        return self.__router

    @property
    def chalice_app(self):
        return self.__app


class AppModule(object):
    __path = ''
    __module = None
    __routers = []
    __test_cases = []

    def __init__(self, path):
        self.__path = path
        self.__module = importlib.import_module(path)
        self.import_all()

    def import_all(self):
        self.import_routes()
        self.import_tests()

    def import_routes(self):
        route_mod = importlib.import_module('.'.join([self.__path, 'routes']))
        try:
            patterns = route_mod.urlpatters
        except AttributeError:
            patterns = []
        self.__routers = patterns

    def import_tests(self):
        try:
            test_mod = importlib.import_module('.'.join([self.__path, 'test']))
        except ImportError:
            return
        for cls_name in dir(test_mod):
            cls = getattr(test_mod, cls_name)
            if self.is_testcase(cls):
                self.__test_cases.append(cls)

    def is_testcase(self, cls):
        try:
            mro = inspect.getmro(cls)
            return unittest.TestCase in mro
        except AttributeError:
            return False

    @property
    def routers(self):
        return self.__routers

    @property
    def test_cases(self):
        return self.__test_cases


__all__ = ['App', 'AppModule']
