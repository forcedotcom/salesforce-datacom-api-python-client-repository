from collections import namedtuple
import json

__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('contact')


class ContactService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def get_contacts(self, contact_ids_list, **kwargs):
        """
        get contacts for the specified ids

        Args:
        contact_ids_list: list (required) list of contact ids
        **kwargs: The other parameters to pass
        """
        #TODO: parse list of contacts from json
        json_str = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        # Parse JSON into an object with attributes corresponding to dict keys.
        contact = json.loads(json_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return [contact]
