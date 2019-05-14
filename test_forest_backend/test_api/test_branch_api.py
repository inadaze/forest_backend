import json
from forest_backend.database.models.branch_model import Branch
from forest_backend.database.sql_db import db

import pytest

headers = {'content-type': 'application/json'}

def test_put_branch_create_new_branch(get_client):
    client, app = get_client
    branch_response = client.put('api/branch', data=json.dumps({'tree_id':1, 'idea': "word"}), headers=headers)
    assert branch_response.status_code == 204

    with app.app.app_context():
        db_branch = db.session.query(Branch).filter(Branch.tree_id==1).first()
        assert db_branch.id == 1


def test_get_branch_returns_requested_branch(get_client):
    client, app = get_client
    branch_response = client.get('api/branch', data=json.dumps({'tree_id': 1, 'idea': "kitten"}), headers=headers)
    assert branch_response.status_code == 200
    branch = json.loads(branch_response.get_data())
    assert branch['data']['id'] == 1

def test_get_branches_returns_all_branches_for_requested_tree(get_client):
    client, app = get_client
    branches_response = client.get('api/branches/1', headers=headers)
    assert branches_response.status_code == 200
    branch = json.loads(branches_response.get_data())
    assert branch['data'][0]['id'] == 1

def test_update_branch_lables_branch_as_cut(get_client):
    client, app = get_client
    branch_response = client.patch('api/branch', data=json.dumps({'id': 1, "cut": True}), headers=headers)
    assert branch_response.status_code == 200

    with app.app.app_context():
        db_branch = db.session.query(Branch).filter(Branch.id==1).first()
        assert db_branch.cut
