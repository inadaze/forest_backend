import pytest
import json

@pytest.fixture
def synonym_response():
    synonyms = None
    response = None
    with open('forest_backend/scheduler/unittests/external_responses/synonyms.json', 'r') as myfile:
        response = RestResponse(myfile.read())

    return response

@pytest.fixture
def get_new_trees_response():
    trees = None
    response = None
    with open('forest_backend/scheduler/unittests/internal_responses/get_new_trees.json', 'r') as myfile:
        response = RestResponse(myfile.read())

    return response

class RestResponse():
    text = None
    def __init__(self, text):
        self.text = text
