import httplib2
import urllib
import json
from datacom.exceptions import DataComApiError

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
        enc_params = urllib.urlencode(params)
        if False:#TODO implement adding parameters to url with params
            url = '%s&%s' % (url, enc_params)
        else:
            url = '%s?%s' % (url, enc_params)

    print url
    resp, content = http.request(url, method, headers=headers, body=data)

    return DataComResponse(resp, content.decode('utf-8'), url)


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
    headers = kwargs.get("headers", {})
    headers["Accept-Charset"] = "utf-8"
    headers["user_client"] = "salesforce-datacom-api-python-client-v1"

    if "Accept" not in headers:
        headers["Accept"] = "application/json"

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    if auth is not None:
        headers["Authorization"] = "BEARER %s" % auth.get_access_token()

    kwargs["headers"] = headers
    print "headers: %s" % kwargs["headers"]
    print "params: %s" % kwargs["params"]

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        #TODO add processing errors and codes
        code = 500
        print "error: %s, content: %s" % (resp.status_code, resp.content)
        raise DataComApiError(resp.status_code, resp.url, "TBD", code)

    print "content: %s" % resp.content

    return resp
