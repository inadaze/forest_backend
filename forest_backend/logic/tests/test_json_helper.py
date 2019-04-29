import json
import pytest
from forest_backend.logic.json_helper import JsonHelper

def test_get_synonyms_returns_list(synonym_response):
    json_helper = JsonHelper()
    json_data = json.loads(synonym_response)
    synonym_list = json_helper.get_synonyms(json_data)

    assert synonym_list == ['very good', 'superb', 'outstanding', 'magnificent', 'of high quality', 'of the highest quality', 'of the highest standard', 'exceptional', 'marvellous', 'wonderful', 'sublime', 'perfect', 'eminent', 'pre-eminent', 'matchless', 'peerless', 'supreme', 'first-rate', 'first-class', 'superior', 'superlative', 'splendid', 'admirable', 'worthy', 'sterling', 'fine']
