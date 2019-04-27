import json
from testfixtures import LogCapture
import pytest

#TODO: can I reuse this code with a fixture's arg instead of repeating it over and over?
@pytest.fixture
def synonym_response():
    response = None
    with open('forest_backend/logic/tests/external_responses/synonyms.json', 'r') as myfile:
        response = RestResponse(myfile.read())
    return response

@pytest.fixture
def get_new_seeds_response():
    response = None
    with open('forest_backend/logic/tests/internal_responses/get_new_seeds.json', 'r') as myfile:
        response = myfile.read()
    return response

@pytest.fixture
def get_level_0_trees_response():
    response = None
    with open('forest_backend/logic/tests/internal_responses/get_level_0_trees.json', 'r') as myfile:
        response = myfile.read()
    return response

@pytest.fixture
def get_focus_synonyms_response():
    response = None
    with open('forest_backend/logic/tests/external_responses/get_focus_synonyms.json', 'r') as myfile:
        response = myfile.read()
    return response

@pytest.fixture
def get_torrent_synonyms_response():
    response = None
    with open('forest_backend/logic/tests/external_responses/get_torrent_synonyms.json', 'r') as myfile:
        response = myfile.read()
    return response

class RestResponse():
    text = None
    def __init__(self, text):
        self.text = text

# @pytest.fixture(autouse=True)
# def capture():
#     with LogCapture() as capture:
#         yield capture
