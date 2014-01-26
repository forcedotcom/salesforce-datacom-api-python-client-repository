from datacom.connect.company_service import CompanyService
from datacom.connect.contact_service import ContactService

__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('main')


class DataComClient(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def contact_service(self):
        return ContactService(self.config_dict)

    def company_service(self):
        return CompanyService(self.config_dict)


if __name__ == '__main__':
  print "Hello from Client"