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

from data import *
from datacom.auth import Auth
from datacom.http_requests import *

__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('datacomconnect')


class CompanyService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.auth = Auth(config_dict)

    #@todo when input is large need to use POST, I think I would always use POST
    def get_companies(self, company_ids_list, **kwargs):
        """
        get companies for the specified ids

        @type company_ids_list: list
        @param company_ids_list: list of company ids in Data.com account (required)
        @type kwargs: dictionary
        @param kwargs: other parameters to pass

        @rtype: CompanyList
        @return: CompanyList contains list of found companies by ids, total number of contacts, page size
        @raise DataComApiError: If response is not 200
        """
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), COMPANIES_GET_URL,
                       ",".join(company_ids_list)])
        headers = {"x-ddc-client-id": self.config_dict.get("x-ddc-client-id")}

        json_response = datacom_http_request("GET", url, auth=self.auth, params=None, headers=headers)

        data = json.loads(json_response)
        return CompanyList(data)

    #@todo parameters can be passed with _, add transforming them to camel case, add ability to use states as CA, TX
    #not numbers
    #@todo deal with arrays for example ownership=1&ownership=2 ability to use
    def search_companies(self, name="", **kwargs):
        """
        search companies by name, additional parameters can be passed as kwargs

        @type name: str
        @param name: full or part of company name, can be empty
        @type kwargs: dictionary
        @param kwargs: The other parameters to pass, see doc: TBD url #TODO

        @rtype: CompanyList
        @return: CompanyList contains list of found companies by ids, total number of contacts, page size
        @raise DataComApiError: If response is not 200
        """

        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), COMPANIES_SEARCH_URL])

        headers = {"x-ddc-client-id": self.config_dict.get("x-ddc-client-id")}
        params = {"name": name}
        params.update(kwargs)
        json_response = datacom_http_request("GET", url, auth=self.auth, params=params, headers=headers)

        data = json.loads(json_response)
        return CompanyList(data)