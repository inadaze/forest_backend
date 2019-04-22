import json
from forest_backend.database.models.seed_model import Seed
from forest_backend.database.sql_db import db


import pytest

def test_returns_a_seed(get_client):
    client, app = get_client
    seeds_response = client.get('api/seeds')
    seeds = json.loads(seeds_response.get_data())

    assert seeds['data'][0]['word'] == "floral"

def test_can_add_a_seed(get_client):
    client, app = get_client
    seeds_response = client.put('api/seed/mexico')
    assert seeds_response.status_code == 204
    
    with app.app.app_context():
        db_seeds = db.session.query(Seed).all()

    assert list(filter(lambda seed: seed.word == 'mexico', db_seeds))
    
    

