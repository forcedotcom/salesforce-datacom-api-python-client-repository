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
from datacom.connect.data import ERRORS_JSON_KEY

__author__ = 'okhylkouskaya'


class DataComError(Exception):
    pass


class DataComApiError(DataComError):
    def __init__(self, status, uri, reason=None, code=None, body=None, headers=None):
        """
        A generic exception from the Data.com API

        @type status: int
        @param status: the HTTP status that was returned for the exception
        @type uri: str
        @param uri: The URI that caused the exception
        @type reason: str
        @param reason: A human-readable message for the error
        @type code: int|None
        @param code: A Data.com-specific error code for the error. This is
             not available for all errors.
        @type body: str
        @param body: (optional) specify if the response has already been read
                      from the http_response object.
        @type headers: str
        @param headers: headers in the request
        """

        self.uri = uri
        self.status = status
        self.reason = reason
        self.code = code
        self.body = body
        self.headers = headers

        if self.code is None and self.reason is None and self.body:
            self._parse_content_4_details(self.body)

    def _parse_content_4_details(self, json_content):
        try:
            error_data = json.loads(json_content)
            errors = error_data.get(ERRORS_JSON_KEY, [])

            messages = ""
            codes = ""
            for error in errors:
                messages += error.get("message", "") + ","
                codes += str(error.get("code", "")) + ","

            self.message = messages
            self.code = codes
        except Exception:
            pass


    def __str__(self):
        return "Generic exception from the Data.com API, status: %s, uri: %s, response: %s, message: %s, code: %s" % \
               (self.status, self.uri, self.body, self.message, self.code)


class BadAuthentication(DataComApiError):
    pass
