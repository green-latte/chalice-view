BASE_RESOURCE_PATH = 'https://localhost'

def req2levent(chalice_app, request):
    # context = {
    #     'api-id': None,
    #     'authorizer': {},
    #     'http-method': request.method,
    #     'identity': {},
    #     'request-id': None,
    #     'resource-id': None,
    #     'resource-path': BASE_RESOURCE_PATH,
    #     'stage': None
    # }
    event = {
        'params': {
            'path': request.context['uri_params'],
            'querystring': request.query_params,
            'header': request.headers
        },
        'body-json': request.json_body,
        'base64-body': request._base64_body,
        'stage-variables': request.stage_vars,
        'context': {
            'resource-path': request.context['path'],
            'http-method': request.method
        }
    }
    context = {}
    return event, context


# For Local API Gateway
# => currently not used
# https://github.com/ToQoz/api-gateway-localdev/blob/master/lib/sort_routes.js
def sort_routes(routes):
    routes_depth = [len(r.split('/')) for r in routes]
    max_depth = max(routes_depth)
    def comparison(a, b):
        al = length(a)
        for i, segment in enumerate(a.split('/')):
            try:
                assert segment.index('{') >= 0
                al += 999 * (max_depth - i)
            except AssertionError:
                pass
        bl = length(b)
        for i, segment in enumerate(b.split('/')):
            try:
                assert segment.index('{') >= 0
                bl += 999 * (max_depth - i)
            except AssertionError:
                pass
        return al - bl
    routes = sorted(routes, cmp=comparison)
    return routes
