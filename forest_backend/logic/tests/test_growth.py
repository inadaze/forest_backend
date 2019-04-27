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
        mock.put(matcher, status_code=204, complete_qs=True)
        
        growth = get_growth
        assert growth.germinate()

def test_sprout_creates_branches_from_tree_word(get_growth, get_level_0_trees_response, get_focus_synonyms_response, get_torrent_synonyms_response):
    with requests_mock.Mocker() as mock:
        mock.get('http://localhost:5000/api/trees', json=json.loads(get_level_0_trees_response), headers={'content-type': 'application/json'})
        
        focus_matcher = re.compile('https://od-api.oxforddictionaries.com/api/v1/entries/en/focus/synonyms')
        mock.get(focus_matcher, json=json.loads(get_focus_synonyms_response), complete_qs=True)

        torrent_matcher = re.compile('https://od-api.oxforddictionaries.com/api/v1/entries/en/torrent/synonyms')
        mock.get(torrent_matcher, json=json.loads(get_torrent_synonyms_response), complete_qs=True)

        growth = get_growth
        assert growth.sprout()
