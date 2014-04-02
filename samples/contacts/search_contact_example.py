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
from datacom.connect.client import DataComClient
from datacom.exceptions import *
import settings

__author__ = 'okhylkouskaya'


class SearchContactsExample(object):
    def __init__(self, debug=False):
        config = {
            'grant_type': 'password',
            'username': 'xxxxxxxx',
            "password": "xxxxxxx",
            'client_secret': "xxxxxx",
            "client_id": "xxxxxx",
            "x-ddc-client-id": "xxxxxxx",
            "server_url": "https://api.data.com/connect"
        }

        self.client = DataComClient(config)

    def run(self):
        try:
            print "Search contact"
            contact_list = self.client.contact_service().search_contacts(country="9000")
            print "total: %s" % contact_list.total
            print contact_list.contacts[0]
        except DataComApiError as e:
            print e
        try:
            print "Getting contacts by 17892515 id"
            contact_list = self.client.contact_service().get_contacts(contact_ids_list=['17892515'])
            print "total: %s" % contact_list.total
        except DataComApiError as e1:
            print e1
        try:
            print "purchase contacts by 25848689 id"
            contact_list = self.client.contact_service().purchase_contacts(contact_ids_list=['25848689'])
            print "total: %s" % contact_list.total
        except DataComApiError as e2:
            print e2


def main():
    """The main function runs the SearchContactsExample application."""
    sample = SearchContactsExample(debug=True)
    sample.run()


if __name__ == '__main__':
    main()
