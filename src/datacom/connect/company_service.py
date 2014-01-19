__author__ = 'okhylkouskaya'

import logging

logger = logging.getLogger('company')


class CompanyService(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def get_companies(self, company_ids_list, **kwargs):
        """
        get companies for the specified ids

        Args:
        company_ids_list: list (required) list of company ids
        **kwargs: The other parameters to pass
        """
        return None
