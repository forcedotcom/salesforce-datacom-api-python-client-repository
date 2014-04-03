# Salesforce Data.com Python REST API
================================

Think the REST API is awesome and powerful, but maybe a bit overwhelming? This native Python implementation aims to keep the implementation simple
while keeping all the power at your fingertips.

# Overview
This Python REST API is a simple library to interact with the REST API.


## Installation

Download the source code
(ZIP)](https://github.com/forcedotcom/salesforce-datacom-api-python-client-repository/zipball/master
 "salesforce-datacome-api-python-client source code") for `salesforce-datacome-api-python-client`, and then run:

    $ python setup.py install

You may need to run the above commands with `sudo`.

# Features
- Contact get
- Contact purchase
- Contact search

# Configuration and authentication
The Python REST API supports only one form of authentication.

## Username and password
If your org allows it (grant_type=password), you can use the client ID, client Secret and your username and password to authenticate.
This is discouraged and the ClientSecret authentication is preferred over this one.

### API Credentials

The `DataComClient` needs your Data.com credentials.

```python
from datacom.connect.client import DataComClient

config = {
            'grant_type': 'password',
            'username': 'xxxx',
            "password": "xxxxx",
            'client_secret': "xxxxx",
            "client_id": "xxxxx",
            "x-ddc-client-id": "xxxxx"
        }
client = DataComClient(config)
```

### Get contacts

```python
from datacom.connect.client import DataComClient
from datacom.exceptions import *

config = {
            'grant_type': 'password',
            'username': 'xxxx',
            "password": "xxxxx",
            'client_secret': "xxxxx",
            "client_id": "xxxxx",
            "x-ddc-client-id": "xxxxx"
        }
client = DataComClient(config)

try:
    contact_list = self.client.contact_service().get_contacts(contact_ids_list=['123'])
    print "total: %s" % contact_list.total
except DataComApiError as e:
    print e
```

### Search contacts

```python
from datacom.connect.client import DataComClient
from datacom.exceptions import *

config = {
            'grant_type': 'password',
            'username': 'xxxx',
            "password": "xxxxx",
            'client_secret': "xxxxx",
            "client_id": "xxxxx",
            "x-ddc-client-id": "xxxxx"
        }
client = DataComClient(config)

try:
    contact_list = self.client.contact_service().search_contacts(first_name="Bob", companyName="Microsoft")
    print "total: %s" % contact_list.total
    print contact_list.contacts[0]
except DataComApiError as e:
    print e
```

### Purchase contacts

```python
from datacom.connect.client import DataComClient
from datacom.exceptions import *

config = {
            'grant_type': 'password',
            'username': 'xxxx',
            "password": "xxxxx",
            'client_secret': "xxxxx",
            "client_id": "xxxxx",
            "x-ddc-client-id": "xxxxx"
        }
client = DataComClient(config)

try:
    contact_list = self.client.contact_service().purchase_contacts(contact_ids_list=['123'])
    print "total: %s" % contact_list.total
except DataComApiError as e:
    print e
```

# License
The BSD 2-Clause License

http://opensource.org/licenses/BSD-2-Clause

See [LICENSE.txt](./LICENSE.txt)