class RouterUnit(object):
    def __init__(self, app, path, methods=[]):
        # generate _register_route
        # see => https://github.com/awslabs/chalice/blob/master/chalice/app.py
        self.router = app.route(path, methods=methods)

    def register(self, view_func):
        # call _register_route
        self.router(view_func)


class BaseRouter(object):
    def __init__(self, app):
        self.__app = app

    def register(self, path, view_cls):
        unit = RouterUnit(self.__app, path, methods=view_cls.http_methods())
        unit.register(view_cls.view_func()(self.__app))

__all__ = ['BaseRouter']
