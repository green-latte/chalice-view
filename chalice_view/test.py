import json
import urllib
import base64

from chalice.app import Request


class ChaliceRequestFactory(object):
    def get(self, path, data=None, headers={}, uri_params={}, **extra):
        querystring = urllib.urlencode(data or {})
        if not data and '?' in path:
            querystring = path.split('?')[1]
        return self.generic('get', path, querystring=querystring, headers=headers, uri_params=uri_params)


    def post(self, path, data=None, headers={}, uri_params={}, **extra):
        return self.generic('post', path, body_json=data, headers=headers, uri_params=uri_params)


    def generic(self, method, path, querystring=None, body_json={}, headers={}, uri_params={}):
        body_json_string = json.dumps(body_json)
        base64_body = base64.b64encode(body_json_string)
        context = {'path': path, 'uri_params': uri_params}
        stage_variables = {}
        return Request(querystring, headers, path, method, body_json, base64_body, context, stage_variables)

    def request(self, *request):
        """args: query_params, headers, uri_params, method, body,
                 base64_body, context, stage_vars"""
        return Request()
