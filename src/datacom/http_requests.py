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


def datacom_http_request(method, uri, **kwargs):
    """
    Make a data.com specific http request. Adds additional headers Throws an error

    :return: An http response
    :rtype: A :class:`DataComResponse` object
    :raises DataComApiError: if the response is a 400 or 500-level response.
    """
    headers = kwargs.get("headers", {})
    headers["Accept-Charset"] = "utf-8"
    headers["UserClient"] = "salesforce-datacom-api-python-client-v1"

    if "Accept" not in headers:
        headers["Accept"] = "application/json"

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    kwargs["headers"] = headers
    print kwargs["headers"]
    print kwargs["params"]

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        #TODO add processing errors and codes
        code = 500
        print "error, content: %s" % resp.content
        raise DataComApiError(resp.status_code, resp.url, "TBD", code)

    return resp
