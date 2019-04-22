import json
from forest_backend.database.models.seed_model import Seed

import pytest

def test_seedapi_returns_a_seed(client):
    seeds_response = client.get('api/seeds')
    seeds = json.loads(seeds_response.get_data())

    assert seeds['data'][0]['word'] == "floral"