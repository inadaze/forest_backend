import json
from testfixtures import LogCapture
import pytest

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

class RestResponse():
    text = None
    def __init__(self, text):
        self.text = text

# @pytest.fixture(autouse=True)
# def capture():
#     with LogCapture() as capture:
#         yield capture
