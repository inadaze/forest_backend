import json
import requests
from forest_backend.logic.json_helper import JsonHelper
from forest_backend.logic.external_api_configs.oxford_dictionary import config
from forest_backend.logic.internal_api_configs.forest_backend import config as forest_config

class Growth(object):
    url = None
    forest_url = None
    headers = {'app_id': '53e47906', "app_key": "d469e72695b750d658d9289f7f580bfd"}
    json_helper = None

    def __init__(self):
        self.url = config['url']
        sefl.forest_url = forest_config['url']
        self.json_helper = JsonHelper()
        print('Growth')

    # first level
    def sprout(self):
        synonym_url = self.url + "excellent" + "/synonyms"
        get_seeds_url = self.forest_url + "seeds"
        new_seeds = request.get(get_seeds_url)
        response = requests.get(synonym_url, headers=self.headers)
        json_data = json.loads(response.text)
        synonyms = self.json_helper.get_synonyms(json_data)
        print(synonyms)
        return synonyms

    def seedling(self):
        pass

    def sapling(self):
        pass

    def mature(self):
        pass

    def ancient(self):
        pass

    # last level
    def snag(self):
        print('Snag')
    
    def get_new_trees(self):
        print('Getting new trees')
