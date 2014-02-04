# salesforce-datacome-api-python-client

Efficient Python client library for accessing Data.com APIs using JSON and OAuth 2.0

## Installation

Download the source code
(ZIP)](https://github.com/forcedotcom/salesforce-datacom-api-python-client-repository/zipball/master
 "salesforce-datacome-api-python-client source code") for `salesforce-datacome-api-python-client`, and then run:

    $ python setup.py install

You may need to run the above commands with `sudo`.

## Getting Started

Getting started with the Data.com API couldn't be easier. Create a
`DataComClient` and you're ready to go.

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