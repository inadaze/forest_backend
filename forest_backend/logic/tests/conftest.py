# from testfixtures import LogCapture
import pytest

@pytest.fixture
def synonym_response():
    return get_mock_response('external_responses/synonyms.json')

@pytest.fixture
def get_new_seeds_response():
    return get_mock_response('internal_responses/get_new_seeds.json')

@pytest.fixture
def get_level_0_trees_response():
    return get_mock_response('internal_responses/get_level_0_trees.json')

@pytest.fixture
def get_focus_synonyms_response():
    return get_mock_response('external_responses/get_focus_synonyms.json')

@pytest.fixture
def get_torrent_synonyms_response():
    return get_mock_response('external_responses/get_torrent_synonyms.json')

def get_mock_response(path):
    with open('forest_backend/logic/tests/' + path, 'r') as myfile:
        return myfile.read()

# @pytest.fixture(autouse=True)
# def capture():
#     with LogCapture() as capture:
#         yield capture
