import json
import pytest
import re
import requests
from forest_backend.logic.growth import Growth
import requests_mock

# TODO: need to have a test logger defined so I can write to it from here 
# and replace the one that was defined in scheduler

@pytest.fixture
def get_growth():
    return Growth()

def test_germinate_creates_tree_from_new_seeds(get_growth, get_new_seeds_response):
    # TODO: need to test that the right messages are logged
    with requests_mock.Mocker() as mock:
        mock.get('http://localhost:5000/api/seeds', json=json.loads(get_new_seeds_response), headers={'content-type': 'application/json'})
        
        matcher = re.compile('http://localhost:5000/api/tree/*')
        mock.put(matcher, status_code=204, complete_qs=True)
        
        growth = get_growth
        assert growth.germinate()
