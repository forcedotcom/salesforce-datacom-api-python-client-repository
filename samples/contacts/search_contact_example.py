from datacom.connect.client import DataComClient

__author__ = 'okhylkouskaya'


class SearchContactsExample(object):
    def __init__(self, debug=False):
        config = {
            'grant_type': 'password',
            'username': 'username',
            'client_id': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
        self.client = DataComClient(config)
        #TODO authentificate

    def run(self):
        print "Getting contacts by 123 id"
        contacts = self.client.contact_service().get_contacts(contact_ids_list=[123])

        print [c.name for c in contacts]


def main():
    """The main function runs the SearchContactsExample application."""

    sample = SearchContactsExample(debug=True)
    sample.run()


if __name__ == '__main__':
    main()
