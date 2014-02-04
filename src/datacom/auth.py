__author__ = 'okhylkouskaya'

"""Provides auth related token classes and functions for Salesforce Data APIs."""

from collections import namedtuple
import json
from datacom.connect.data import *
from datacom.http_requests import *

__author__ = 'okhylkouskaya'


class Auth(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.access_token = None
        self.refresh_token = None
        self.expires_in = None
        self.scope = None

    def get_access_token(self):
        print "in get access token"
        if self.access_token is None:
            self.request_access_token()

        return self.access_token

    def request_access_token(self):
        print "in request access token"
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), OAUTH2_TOKEN_URL])
        params = {"client_id": self.config_dict.get("client_id"), "client_secret": "secret",
                  'grant_type': self.config_dict.get("grant_type"), 'username': self.config_dict.get("username"),
                  "password": self.config_dict.get("password")}

        datacom_response = auth_http_request("GET", url, params=params)
        json_str = datacom_response.content
        token_info = json.loads(json_str)

        self.access_token = token_info["access_token"]
        self.refresh_token = token_info["refresh_token"]
        self.expires_in = token_info["expires_in"]
        self.scope = token_info["scope"]

        print "access token: %s" % self.access_token

        return self.access_token