import inspect

from chalice import NotFoundError


def project(dict, keys=[]):
    new_dict = {}
    for k in keys:
        v = dict.get(k)
        if v:
            new_dict.update({k: v})
    return new_dict

def get_class_that_defined_method(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__:
            return cls
    return None

def wrap(view_funcs):
    def before_request(app): # todo change name
        def view_wrapper(*args, **kwargs):
            request = app.current_request
            # get 'get' or 'post' function <-- just pointer of function in class
            # and next, create instance and get method pointer of instance
            view_func = view_funcs.get(request.method)
            view_cls = get_class_that_defined_method(view_func)
            view_instance = view_cls()
            view_func = getattr(view_instance, request.method)
            if view_func:
                return view_func(request, *args, **kwargs)
            else:
                raise NotFoundError()
        return view_wrapper
    return before_request


class View(object):
    BASE_METHODS = ['get', 'post']

    @classmethod
    def get_or_post_functions(cls):
        funcs = inspect.getmembers(cls, predicate=inspect.ismethod)
        funcs = dict(funcs)
        funcs = project(funcs, cls.BASE_METHODS)
        return funcs

    @classmethod
    def view_func(cls):
        return wrap(cls.get_or_post_functions())

    @classmethod
    def http_methods(cls):
        return cls.get_or_post_functions().keys()

    @classmethod
    def as_view(cls):
        return cls.recieve_request

    @classmethod
    def recieve_request(cls, request):
        print 'accepted'


__all__ = ['View']
