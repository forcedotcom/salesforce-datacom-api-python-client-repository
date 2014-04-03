import json

__author__ = 'okhylkouskaya'

import unittest

#@todo use mock
#from mock import Mock, patch

from tools import *
from datacom.connect.data import Contact, ContactList


class ContactsTest(unittest.TestCase):
    def test_list_contacts(self):
        resp = read_json("contacts_list.json")

        contact_list = ContactList(resp)

        self.assertIsNotNone(contact_list)
        self.assertIsNotNone(contact_list.contacts)
        self.assertEquals(contact_list.total, 5)
        self.assertEquals(contact_list.size, 3)
        self.assertEquals(contact_list.page_num, 1)
        self.assertEquals(contact_list.contacts[0].contactId, 19950919)
        self.assertEquals(contact_list.contacts[0].firstName, "Ryna")

    def test_list_contacts_empty_json(self):
        resp = None
        contact_list = ContactList(resp)
        self._assertEmptyJson(contact_list)

        resp = "{}"
        contact_list = ContactList(resp)
        self._assertEmptyJson(contact_list)

        resp = '{"totalHits":0,"contacts":[]}'
        contact_list = ContactList(resp)
        self._assertEmptyJson(contact_list)

        resp = '{"totalHits_not_known":5,"contacts":[]}'
        contact_list = ContactList(resp)
        self._assertEmptyJson(contact_list)

        resp = '{"totalHits":0,"contacts_not_known":[]}'
        contact_list = ContactList(resp)
        self._assertEmptyJson(contact_list)


    def _assertEmptyJson(self, contact_list):
        self.assertIsNotNone(contact_list)
        self.assertIsNotNone(contact_list.contacts)
        self.assertEquals(contact_list.total, 0)
        self.assertEquals(contact_list.size, 0)
        self.assertEquals(contact_list.page_num, 1)


def suite():
    return build_suite([ContactsTest])


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

