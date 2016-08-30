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


class Router(object):
    def __init__(self, path, view_cls, namespace):
        self.path = path
        self.view_cls = view_cls
        self.namespace = namespace


def url(path, view_cls, namespace=''):
    return Router(path, view_cls, namespace)


__all__ = ['BaseRouter', 'url']
