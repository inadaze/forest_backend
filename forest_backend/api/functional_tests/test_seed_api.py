import json
from forest_backend.database.models.seed_model import Seed
from forest_backend.database.sql_db import db


import pytest

headers = {'content-type': 'application/json'}

def test_get_seed_returns_a_seed(get_client):
    client, app = get_client
    seeds_response = client.get('api/seeds')
    seeds = json.loads(seeds_response.get_data())

    assert seeds['data'][0]['word'] == "floral"

def test_put_seed_with_list_args_can_add_a_seed(get_client):
    client, app = get_client

    seeds_response = client.put('api/seed/mexico', data=json.dumps(None), headers=headers)
    assert seeds_response.status_code == 204
    
    with app.app.app_context():
        db_seeds = db.session.query(Seed).all()

    assert list(filter(lambda seed: seed.word == 'mexico', db_seeds))

def test_put_seed_with_payload_can_add_a_seed(get_client):
    client, app = get_client
    data = {"word": "tent"}
    seeds_response = client.put('api/seed/', data=json.dumps(data), headers=headers)
    assert seeds_response.status_code == 204
    
    with app.app.app_context():
        db_seeds = db.session.query(Seed).all()

    assert list(filter(lambda seed: seed.word == 'tent', db_seeds))

def test_put_seed_returns_error_when_no_seed_specified(get_client):
    client, app = get_client
    data = {"word": ""}
    seeds_response = client.put('api/seed/', data=json.dumps(data), headers=headers)
    assert seeds_response.status_code == 400
    