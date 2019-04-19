import pytest
import requests
from forest_backend.logic.growth import Growth

@pytest.fixture
def get_growth():
    return Growth()

def test_sprout_fetches_synonyms(mocker, get_growth, synonym_response):
    mocker.patch('requests.get', return_value=synonym_response)
    growth = get_growth
    synonyms = growth.sprout()
    assert synonyms == ['very good', 'superb', 'outstanding', 'magnificent', 'of high quality', 'of the highest quality', 'of the highest standard', 'exceptional', 'marvellous', 'wonderful', 'sublime', 'perfect', 'eminent', 'pre-eminent', 'matchless', 'peerless', 'supreme', 'first-rate', 'first-class', 'superior', 'superlative', 'splendid', 'admirable', 'worthy', 'sterling', 'fine']

def test_can_get_new_seeds(mocker, get_new_trees_response):
    mocker.patch('requests.get', return_value=get_new_trees_response)