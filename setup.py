#!/usr/bin/python
#
# Copyright (C) 2013 Salesforce.com.
#
# //TODO add license

import sys
from setuptools import setup, find_packages
#from distutils.core import setup

# python setup.py install

required = ['httplib2']

setup(
    name='datacomclient',
    version='1.0',
    description='Python client library for Salesforce data APIs',
    long_description="""\
The Salesforce data Python client library makes it easy to interact with
data.com services through the Salesforce Data APIs. This library provides data
models and service modules for the the following Salesforce data services:
- Connect API
The core Salesforce data code provides sufficient functionality to use this
library with any data.com API.
""",
    author='Olga Khylkouskaya',
    author_email='okhylkouskaya@salesforce.com',
    license='Apache 2.0',
    url='http://github.com/python-client/',
    install_requires=required,
    packages = [
      'datacom',
      'datacom.connect'
    ],
    package_dir={'datacom': 'src/datacom'},
    include_package_data=True
)
