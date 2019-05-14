import json
from forest_backend.database.models.tree_model import Tree
from forest_backend.database.sql_db import db


import pytest

headers = {'content-type': 'application/json'}

def test_get_trees_returns_a_tree(get_client):
    client, app = get_client
    trees_response = client.get('api/trees')
    trees = json.loads(trees_response.get_data())

    assert trees['data'][0]['seed']['word'] == "floral"

def test_get_trees_returns_new_trees(get_client):
    client, app = get_client
    data = {"level_id": 0}
    trees_response = client.get('api/trees', data=json.dumps(data), headers=headers)
    trees = json.loads(trees_response.get_data())

    assert trees['data'][0]['seed']['word'] == "floral"

def test_get_trees_returns_different_level_trees(get_client):
    client, app = get_client
    data = {"level_id": 1}
    trees_response = client.get('api/trees', data=json.dumps(data), headers=headers)
    trees = json.loads(trees_response.get_data())

    assert trees['data'][0]['seed']['word'] == "minimal"

def test_get_tree_by_seed_word(get_client):
    client, app = get_client
    tree_response = client.get('api/tree/'+'floral')
    tree = json.loads(tree_response.get_data())

    assert tree['data']['id'] == 1

def test_put_tree_can_add_tree_by_seed_id(get_client):
    client, app = get_client
    tree_response = client.put('api/tree/'+'temptation')
    assert tree_response.status_code == 204

    with app.app.app_context():
        db_trees = db.session.query(Tree).all()
        tree = list(filter(lambda tree: tree.seed.word == 'temptation', db_trees))

    assert tree[0].id == 3

def test_put_tree_returns_error_if_seed_does_not_exist(get_client):
    client, app = get_client
    tree_response = client.put('api/tree/'+'temptations')
    assert tree_response.status_code == 404

def test_patch_tree_updates_tree_level(get_client):
    client, app = get_client
    tree_response = client.patch('api/tree', data=json.dumps({'id': 1, 'level_id':1}), headers=headers)
    assert tree_response.status_code == 200

    with app.app.app_context():
        db_tree = db.session.query(Tree).filter(Tree.id==1).first()
        assert db_tree.level_id == 1

def test_get_tree_returns_only_non_cut_branches(get_client):
    client, app = get_client
    tree_response = client.get('api/tree/'+'floral')
    tree = json.loads(tree_response.get_data())

    assert len(tree['data']['branch']) == 1
    assert tree['data']['branch'][0]['idea'] == "kitten"
