__author__ = 'okhylkouskaya'

class Test1(object):
    def test_test(self):
        return None

def make_request(method, url, params=None, data=None, headers=None,
                 cookies=None, files=None, auth=None, timeout=None,
                 allow_redirects=False, proxies=None):
    """Sends an HTTP request

    :param str method: The HTTP method to use
    :param str url: The URL to request
    :param dict params: Query parameters to append to the URL
    :param dict data: Parameters to go in the body of the HTTP request
    :param dict headers: HTTP Headers to send with the request
    :param float timeout: Socket/Read timeout for the request

    :return: An requests response
    :rtype: A :class:`requests` object

    See the requests documentation for explanation of all these parameters

    Currently proxies, files, and cookies are all ignored
    """