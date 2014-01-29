from collections import namedtuple
import json
from data import *
from datacom.auth import Auth
from datacom.http_requests import *

__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('contact')


class ContactService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.auth = Auth(config_dict)

    def get_contacts(self, contact_ids_list, **kwargs):
        """
        get contacts for the specified ids

        Args:
        contact_ids_list: list (required) list of contact ids
        **kwargs: The other parameters to pass
        On failure, a DataComApiError is raised of the form:
        {'status': HTTP status code from server,
         'uri':The URI that caused the exception
         'reason': HTTP reason from the server,
         'code': A Data.com-specific error code for the error
         'body': HTTP body of the server's response}
         'headers':headers in the request
        """
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), CONTACTS_GET_URL, ",".join(contact_ids_list)])
        headers = {"x-ddc-client-id": self.config_dict.get("x-ddc-client-id")}

        json_str = datacom_http_request("GET", url, auth=self.auth, params=None, headers=headers)

        #TODO: parse list of contacts from json
        json_str = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        # Parse JSON into an object with attributes corresponding to dict keys.
        contact = json.loads(json_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return [contact]

    def search_contacts(self, first_name=None, last_name=None, email=None, **kwargs):
        """
        search contact by first_name and/or email and/or last_name, additional parameters can be passed as kwargs

        Args:
        first_name: full or part of first name, can be empty
        email: full or part of email, can be empty
        last_name: full or part of last name, can be empty
        **kwargs: The other parameters to pass, see doc: TBD url #TODO

        On failure, a DataComApiError is raised of the form:
        {'status': HTTP status code from server,
         'uri':The URI that caused the exception
         'reason': HTTP reason from the server,
         'code': A Data.com-specific error code for the error
         'body': HTTP body of the server's response}
         'headers':headers in the request
        """
        url = "".join([self.config_dict.get("server_url", DEFAULT_BASE_URI), CONTACTS_SEARCH_URL])

        headers = {"x-ddc-client-id": self.config_dict.get("x-ddc-client-id")}
        params = {"email": email, "firstName": first_name, "lastName": last_name}
        params.update(kwargs)
        json_str = datacom_http_request("GET", url, auth=self.auth, params=params, headers=headers)

        #TODO: parse list of contacts from json
