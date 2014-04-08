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

__author__ = 'okhylkouskaya'


#@todo use mock
#from mock import Mock, patch


import unittest
from tools import *
from datacom.connect.data import ContactList


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

