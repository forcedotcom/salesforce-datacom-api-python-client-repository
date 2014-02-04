"""Data model classes for parsing and generating json for the Contacts API."""

__author__ = 'okhylkouskaya'

import datetime

DEFAULT_BASE_URI = "https://api.jigsaw.com/connect"

OAUTH2_TOKEN_URL = "/oauth2/token"
CONTACTS_GET_URL = "/data/v3/contacts/get/"
CONTACTS_PURCHASE_URL = "/data/v3/contacts/purchase/"
CONTACTS_SEARCH_URL = "/data/v3/contacts/search"

CONTACTS_JSON_KEY = "contacts"
TOTAL_JSON_KEY = "totalHits"
JSON_DATE_FIELD_NAMES = ["updatedDate"]

DEFAULT_PAGE_SIZE = 200

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


class Contact(object):
    def __init__(self, attributes_json):
        for key in attributes_json.keys():
            if key in JSON_DATE_FIELD_NAMES and isinstance(attributes_json[key], str):
                attributes_json[key] = datetime.datetime.strptime(attributes_json[key], DATE_FORMAT)

        self.__dict__.update(attributes_json)

    def __str__(self):
        return self.firstName + " " + self.lastName


class ContactList(object):
    def __init__(self, list_response_json):
        self.contacts = []
        self.page_size = DEFAULT_PAGE_SIZE
        self.page_num = 1
        self.total = list_response_json.get(TOTAL_JSON_KEY, None)

        contact_list = list_response_json[CONTACTS_JSON_KEY]
        for contact_json in contact_list:
            self.contacts.append(Contact(contact_json))

        if self.total is None:
            self.total = len(self.contacts)