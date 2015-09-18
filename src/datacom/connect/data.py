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
from decimal import Decimal
import json

"""Data model classes for parsing and generating json for the Contacts API."""

__author__ = 'okhylkouskaya'

import datetime

DEFAULT_BASE_URI = "https://api.data.com/connect"

OAUTH2_TOKEN_URL = "/oauth2/token"

CONTACTS_GET_URL = "/data/v3/contacts/get/"
CONTACTS_PURCHASE_URL = "/data/v3/contacts/purchase/"
CONTACTS_SEARCH_URL = "/data/v3/contacts/search"

USER_INFO_URL = "/data/v5/users/getinfo"
AUTOSUGGEST_URL = "/data/v5/search/autosuggest"
BIZ_CARD_SCAN_URL = "/data/v5/contacts/scanbusinesscard"

COMPANIES_GET_URL = "/data/v3/companies/get/"
COMPANIES_SEARCH_URL = "/data/v3/companies/search"

COMPANIES_JSON_KEY = "companies"
CONTACTS_JSON_KEY = "contacts"
TOTAL_JSON_KEY = "totalHits"
JSON_DATE_FIELD_NAMES = ["updatedDate"]

ERRORS_JSON_KEY = "errors"

DEFAULT_PAGE_SIZE = 200

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


class SingleResource(object):
    def __init__(self, attributes_json):
        for key in attributes_json.keys():
            if key in JSON_DATE_FIELD_NAMES and isinstance(attributes_json[key], str):
                attributes_json[key] = datetime.datetime.strptime(attributes_json[key], DATE_FORMAT)

        self.__dict__.update(attributes_json)


class ListResource(object):
    def __init__(self, list_response_json, list_obj, list_obj_json_key, pagesize=DEFAULT_PAGE_SIZE):
        if list_response_json is None:
            list_response_json = "{}"
        list_data = json.loads(list_response_json, parse_float=Decimal)

        self.page_size = DEFAULT_PAGE_SIZE
        self.page_num = 1
        self.total = 0
        self.size = 0

        if list_data is not None:
            self.total = list_data.get(TOTAL_JSON_KEY, None)

            json_list = list_data.get(list_obj_json_key, [])
            if json_list is not None:
                for obj_json in json_list:
                    list_obj.append(self.create_resource(obj_json))

            if self.total is None:
                self.total = len(list_obj)
            self.size = len(list_obj)

    def create_resource(self, obj_json):
        pass


class Contact(SingleResource):
    def __init__(self, attributes_json):
        super(Contact, self).__init__(attributes_json)

    def __str__(self):
        return self.firstName + " " + self.lastName


class ContactList(ListResource):
    def __init__(self, list_response_json):
        self.contacts = []
        super(ContactList, self).__init__(list_response_json, self.contacts, CONTACTS_JSON_KEY)

    def create_resource(self, obj_json):
        return Contact(obj_json)


class Company(SingleResource):
    def __init__(self, attributes_json):
        super(Company, self).__init__(attributes_json)

    def __str__(self):
        return self.name


class CompanyList(ListResource):
    def __init__(self, list_response_json):
        self.companies = []
        super(CompanyList, self).__init__(list_response_json, self.companies, COMPANIES_JSON_KEY)

    def create_resource(self, obj_json):
        return Company(obj_json)