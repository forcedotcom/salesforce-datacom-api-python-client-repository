import httplib2
import urllib
import urlparse
import json
from datacom.exceptions import *

__author__ = 'okhylkouskaya'


class DataComResponse(object):
    """
    create DataComResponse from httplib2 response
    """

    def __init__(self, httplib2_response, content, url):
        self.content = content
        self.status_code = int(httplib2_response.status)
        self.ok = self.status_code < 400
        self.url = url

    def __str__(self):
        return "status code %s, content: %s" % (self.status_code, self.content)


def is_auth_error_status_code(status_code):
    return status_code == 401


def get_datacom_headers(method="GET", additional_headers=None):
    headers = {}
    if additional_headers is not None:
        headers = additional_headers

    headers["Accept-Charset"] = "utf-8"
    headers["user_client"] = "salesforce-datacom-api-python-client-v1"

    if "Accept" not in headers:
        headers["Accept"] = "application/json"

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    return headers


def make_http_request(method, url, params=None, data=None, cookies=None, headers=None, timeout=None):
    """Sends an http request

    :param str method: The http method to use
    :param str url: Complete url to request
    :param dict params: Query parameters for get requests
    :param dict data: Parameters for the body of the http request(post)
    :param dict headers: http Headers to send
    :param float timeout: Connect/Read timeout for the request

    :return: An http response
    :rtype: A :class:`DataComResponse` object
    """
    http = httplib2.Http(timeout=timeout)

    if data is not None:
        data = urllib.urlencode(data)

    if params is not None:
        enc_params = urllib.urlencode(params, doseq=True)
        if urlparse.urlparse(url).query:
            url = '%s&%s' % (url, enc_params)
        else:
            url = '%s?%s' % (url, enc_params)

    resp, content = http.request(url, method, headers=headers, body=data)

    return DataComResponse(resp, content.decode('utf-8'), url)


def auth_http_request(method, uri, **kwargs):
    """
    Make a data.com specific auth http request. Adds additional headers Throws an error

    :return: An http response
    :rtype: A :class:`DataComResponse` object
    :rtype A :class: `datacom.Auth` object
    :raises BadAuthentication: if the response is a 400 or 500-level response.
    """
    print "in datacom_auth_http_request"
    kwargs["headers"] = get_datacom_headers(method, kwargs.get("headers"))

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        #TODO check response and add correct parsing
        try:
            error = json.loads(resp.content)
            code = error["code"]
            message = "%s: %s" % (code, error["message"])
        except:
            code = None
            message = resp.content

        raise BadAuthentication(resp.status_code, resp.url, reason=message, code=code, body=resp.content)

    return resp


def datacom_http_request(method, uri, auth=None, **kwargs):
    """
    Make a data.com specific http request. Adds additional headers Throws an error

    :return: An http response
    :rtype: A :class:`DataComResponse` object
    :param auth  auth class to handle authentification
    :rtype A :class: `datacom.Auth` object
    :raises DataComApiError: if the response is a 400 or 500-level response.
    """
    print "in datacom_http_request"
    kwargs["headers"] = get_datacom_headers(method, kwargs.get("headers"))

    headers = kwargs["headers"]
    if auth is not None:
        headers["Authorization"] = "BEARER %s" % auth.get_access_token()

    print "headers: %s" % kwargs["headers"]
    print "params: %s" % kwargs["params"]

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        #TODO check response and add correct parsing
        try:
            error = json.loads(resp.content)
            code = error["code"]
            message = "%s: %s" % (code, error["message"])
        except:
            code = None
            message = resp.content

        if is_auth_error_status_code(resp.status_code):
            if auth is not None:
                headers["Authorization"] = "BEARER %s" % auth.request_access_token()
                resp = make_http_request(method, uri, **kwargs)

        if not resp.ok:
            raise DataComApiError(resp.status_code, resp.url, body=resp.content)

    print "content: %s" % resp.content

    return resp.content
