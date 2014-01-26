"""Data model classes for parsing and generating json for the Contacts API."""

__author__ = 'okhylkouskaya'

DEFAULT_BASE_URI = "https://api.jigsaw.com/connect"

OAUTH2_TOKEN_URL = "/oauth2/token"
CONTACTS_GET_URL = "/data/v3/contacts/get/"
CONTACTS_PURCHASE_URL = "/data/v3/contacts/purchase/"
CONTACTS_SEARCH_URL = "/data/v3/contacts/search"

class Contact(object):
    pass
