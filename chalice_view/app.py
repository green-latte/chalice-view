from chalice import Chalice

from .router import BaseRouter


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


__all__ = ['App']
