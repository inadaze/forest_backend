import json
from forest_backend.database.models.tree_model import Tree
from forest_backend.database.sql_db import db


import pytest

headers = {'content-type': 'application/json'}

def test_get_tree_returns_a_tree(get_client):
    #TODO: write more unit tests
    client, app = get_client
    trees_response = client.get('api/trees')
    trees = json.loads(trees_response.get_data())

    assert trees['data'][0]['word'] == "floral"

# def test_put_seed_with_list_args_can_add_a_seed(get_client):
#     client, app = get_client

#     seeds_response = client.put('api/seed/mexico', data=json.dumps(None), headers=headers)
#     assert seeds_response.status_code == 204
    
#     with app.app.app_context():
#         db_seeds = db.session.query(Seed).all()

#     assert list(filter(lambda seed: seed.word == 'mexico', db_seeds))
