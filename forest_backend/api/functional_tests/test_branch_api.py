import json
from forest_backend.database.models.branch_model import Branch
from forest_backend.database.sql_db import db

import pytest

headers = {'content-type': 'application/json'}

def test_put_branch_create_new_branch(get_client):
    client, app = get_client
    branch_response = client.get('api/branch/floral')
    branch = json.loads(branch_response.get_data())

    assert branch['data']['id'] == 1