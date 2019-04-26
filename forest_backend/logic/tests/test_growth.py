import json
import pytest
import re
import requests
from forest_backend.logic.growth import Growth
import requests_mock


@pytest.fixture
def get_growth():
    return Growth()

def test_germinate_creates_tree_from_new_seeds(get_growth, get_new_seeds_response):
    with requests_mock.Mocker() as mock:
        mock.get('http://localhost:5000/api/seeds', json=json.loads(get_new_seeds_response), headers={'content-type': 'application/json'})
        
        matcher = re.compile('http://localhost:5000/api/tree/*')
        mock.get(matcher, status_code=204, complete_qs=True)
        
        growth = get_growth
        assert growth.germinate()

