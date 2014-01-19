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
            'username': 'username',
            'client_id': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
client = DataComClient(config)
```

### Get contacts

```python
from datacom.connect.client import DataComClient

config = {
            'grant_type': 'password',
            'username': 'username',
            'client_id': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
client = DataComClient(config)

contacts = self.client.contact_service().get_contacts(contact_ids_list=[123])
print [c.name for c in contacts]
```