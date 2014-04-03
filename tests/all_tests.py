__author__ = 'okhylkouskaya'

import unittest
import test_parsing_contacts_json


def suite():
    return unittest.TestSuite((
        test_parsing_contacts_json.suite()
    ))


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

