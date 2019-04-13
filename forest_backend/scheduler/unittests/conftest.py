import pytest
import json

@pytest.fixture
def synonym_response():
    synonyms = None
    response = None
    with open('forest_backend/scheduler/unittests/responses/synonyms.json', 'r') as myfile:
        response = RestResponse(myfile.read())

    return response

class RestResponse():
    text = None
    def __init__(self, text):
        self.text = text
