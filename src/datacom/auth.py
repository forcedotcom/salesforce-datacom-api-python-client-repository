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
import json

"""Provides auth related token classes and functions for Salesforce Data APIs."""

__author__ = 'okhylkouskaya'

import logging
from datacom.connect.data import *
from datacom.http_requests import *

logger = logging.getLogger('datacomconnect')


class Auth(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.access_token = None
        self.refresh_token = None
        self.expires_in = None
        self.scope = None

    def get_access_token(self):
        if self.access_token is None:
            self.request_access_token()

        return self.access_token

    def request_access_token(self):
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), OAUTH2_TOKEN_URL])
        client_id = self.config_dict.get("client_id")
        username = self.config_dict.get("username")
        params = {"client_id": client_id, "client_secret": "secret", 'grant_type': self.config_dict.get("grant_type"),
                  'username': username, "password": self.config_dict.get("password")}

        logger.info("request access token by url: %s, with client_id: %s, username: %s" % (url, client_id, username))

        datacom_response = auth_http_request("GET", url, params=params)
        json_str = datacom_response.content
        token_info = json.loads(json_str)

        self.access_token = token_info["access_token"]
        self.refresh_token = token_info["refresh_token"]
        self.expires_in = token_info["expires_in"]
        self.scope = token_info["scope"]

        logger.info("access token: %s" % self.access_token)

        return self.access_token