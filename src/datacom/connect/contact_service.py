from collections import namedtuple
import json
from data import *
from datacom.connect.auth_service import AuthService
from datacom.http_requests import *

__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('contact')


class ContactService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.auth_service = AuthService(config_dict)

    def get_contacts(self, contact_ids_list, additional_headers=None, **kwargs):
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

        access_token = self.auth_service.get_access_token()
        print access_token
        headers = {"x-ddc-client-id": self.config_dict.get("x-ddc-client-id"), "Authorization": "BEARER %s" % access_token}
        json_str = datacom_http_request("GET", url, params=None, headers=headers)
        print json_str
        #TODO: parse list of contacts from json
        json_str = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        # Parse JSON into an object with attributes corresponding to dict keys.
        contact = json.loads(json_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return [contact]
