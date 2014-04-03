"""
  Copyright (c) 2014, salesforce.com, inc.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification, are permitted provided
  that the following conditions are met:

     Redistributions of source code must retain the above copyright notice, this list of conditions and the
     following disclaimer.

     Redistributions in binary form must reproduce the above copyright notice, this list of conditions and
     the following disclaimer in the documentation and/or other materials provided with the distribution.

     Neither the name of salesforce.com, inc. nor the names of its contributors may be used to endorse or
     promote products derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
  WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
  PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
  TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE.
"""

import httplib2
import urllib
import urlparse
import logging
from datacom.exceptions import *

__author__ = 'okhylkouskaya'


logger = logging.getLogger('datacomconnect')


class DataComResponse(object):
    """
    create DataComResponse from httplib2 response
    """

    def __init__(self, httplib2_response, content, url):
        self.content = content
        self.status_code = int(httplib2_response.status)
        self.ok = self.status_code == 200
        self.url = url

    def __str__(self):
        return "status code %s, content: %s" % (self.status_code, self.content)


def _is_auth_error_status_code(status_code):
    return status_code == 401


def _get_datacom_headers(method="GET", additional_headers=None):
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
    """
    Sends an http request

    @type method: str
    @param method: The http method to use, possible values are [GET, POST]
    @type params: dictionary
    @param params: Query parameters for get requests
    @type data: dictionary
    @param data: Parameters for the body of the http request(post)
    @type headers: dictionary
    @param headers: http headers to send
    @type timeout: float
    @param timeout: Connect/Read timeout for the request

    @rtype: DataComResponse
    @return: DataComResponse
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
    Make a data.com specific auth http request. Adds additional headers
    Raises BadAuthentication exception if the response is a 400 or 500-level response.

    @type method: str
    @param method: The http method to use, possible values are [GET, POST]
    @type uri: str
    @param uri: auth uri
    @type kwargs: dictionary
    @param kwargs: other parameters to pass

    @rtype: DataComResponse
    @return: DataComResponse
    @raise BadAuthentication: If response is not 200
    """

    kwargs["headers"] = _get_datacom_headers(method, kwargs.get("headers"))

    logger.debug("auth request headers: %s" % kwargs["headers"])

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        raise BadAuthentication(resp.status_code, resp.url, body=resp.content)

    return resp


def datacom_http_request(method, uri, auth=None, **kwargs):
    """
    Sends a Data.com specific http request

    @type method: str
    @param method: The http method to use, possible values are [GET, POST]
    @type uri: str
    @param uri: uri
    @type auth: Auth
    @param auth: Auth object after auth request
    @type kwargs: dictionary
    @param kwargs: other parameters to pass

    @rtype: DataComResponse
    @return: DataComResponse
    @raise DataComApiError: If response is not 200
    """
    kwargs["headers"] = _get_datacom_headers(method, kwargs.get("headers"))

    headers = kwargs["headers"]
    if auth is not None:
        headers["Authorization"] = "BEARER %s" % auth.get_access_token()

    logger.debug("datacom_http_request request headers: %s" % kwargs["headers"])
    logger.debug("datacom_http_request request params: %s" % kwargs["params"])

    resp = make_http_request(method, uri, **kwargs)

    if not resp.ok:
        if _is_auth_error_status_code(resp.status_code):
            logger.info("Auth error status code: %s, will try to request another access token") % (resp.status_code,)
            if auth is not None:
                headers["Authorization"] = "BEARER %s" % auth.request_access_token()
                resp = make_http_request(method, uri, **kwargs)

        if not resp.ok:
            raise DataComApiError(resp.status_code, resp.url, body=resp.content)

    logger.debug("datacom_http_request response content: %s" % resp.content)

    return resp.content
