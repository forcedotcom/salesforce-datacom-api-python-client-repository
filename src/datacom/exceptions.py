__author__ = 'okhylkouskaya'


class Error(Exception):
    pass


class DataComApiError(Error):
    """ A generic 400 or 500 level exception from the Data.com API

    :param int status: the HTTP status that was returned for the exception
    :param str uri: The URI that caused the exception
    :param str reason: A human-readable message for the error
    :param int|None code: A Data.com-specific error code for the error. This is
         not available for all errors.
    :param body: str (optional) specify if the response has already been read
                  from the http_response object.
    :param headers: str(optional) headers in the request
    """

    def __init__(self, status, uri, reason="", code=None, body=None, headers=None):
        self.uri = uri
        self.status = status
        self.reason = reason
        self.code = code
        self.body = body
        self.headers = headers

    def __str__(self):
        return "Generic 400 or 500 level exception from the Data.com API %s: %s \n %s" % (self.status, self.reason, self.uri)


class BadAuthentication(DataComApiError):
    pass