from __future__ import with_statement
import unittest
from mock import Mock

__author__ = 'okhylkouskaya'


def build_suite(classes):
    """
    Creates a TestSuite for all unit test classes in the list.

    Assumes that each of the classes in the list has unit test methods which
    begin with 'test'. Calls unittest.makeSuite.

    Returns:
      A new unittest.TestSuite containing a test suite for all classes.
    """
    suites = [unittest.makeSuite(a_class, 'test') for a_class in classes]
    return unittest.TestSuite(suites)


def create_mock_json(path):
    with open(path) as f:
        resp = Mock()
        resp.content = f.read()
        return resp


def read_json(json_file_name):
    with open("tests/resources/" + json_file_name) as f:
        return f.read()