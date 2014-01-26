from collections import namedtuple
import json
from data import *
from datacom.http_requests import *

__author__ = 'okhylkouskaya'


class AuthService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.access_token = None

    def get_access_token(self):
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), OAUTH2_TOKEN_URL])
        params = {"client_id": self.config_dict.get("client_id"), "client_secret": "secret",
                  'grant_type': self.config_dict.get("grant_type"), 'username': self.config_dict.get("username"),
                  "password": self.config_dict.get("password")}

        datacom_response = datacom_http_request("GET", url, params=params)
        json_str = datacom_response.content
        token_info = json.loads(json_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        return token_info.access_token