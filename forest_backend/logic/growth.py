import json
import logging
import requests
from forest_backend.logic.json_helper import JsonHelper
from forest_backend.logic.external_api_configs.oxford_dictionary import config
from forest_backend.logic.internal_api_configs.forest_backend import config as forest_config


logger = logging.getLogger('forest_backend_scheduler')

class Growth(object):
    url = None
    forest_url = None
    headers = {'app_id': '53e47906', "app_key": "d469e72695b750d658d9289f7f580bfd"}
    json_helper = None

    def __init__(self):
        self.url = config['url']
        self.forest_url = forest_config['url']
        self.forest_headers = forest_config['headers']
        self.json_helper = JsonHelper()
        print('Growth')

    # grow a seed into a new tree
    def germinate(self):
        print("germ")
        get_seeds_url = self.forest_url + "seeds"
        new_seeds = requests.get(get_seeds_url, data=json.dumps({"tree_level": 0}), headers=self.forest_headers).json()

        for seed in new_seeds['data']:
            put_tree_url = self.forest_url + "tree/" + seed['word']
            status = requests.put(put_tree_url, headers=self.forest_headers).status_code
            if status != 204:
                logger.debug('Seed with the word %s did not germinate into a tree', seed['word'])
        return True

    # first level level 0 to level 1
    def sprout(self):
        #TODO: fetch all new trees and turn into sprouts
        get_seeds_url = self.forest_url + "seeds"
        data = {"tree_level": 0}
        new_seeds = requests.get(get_seeds_url, data=json.dumps(data), headers=self.forest_headers)
        synonym_url = self.url + "excellent" + "/synonyms"

        response = requests.get(synonym_url, headers=self.headers)
        json_data = json.loads(response.text)
        synonyms = self.json_helper.get_synonyms(json_data)
        print(synonyms)
        return synonyms

    #  :level 1 to level 2
    def seedling(self):
        pass

    #  :level 2 to level 3
    def sapling(self):
        pass

    #  :level 3 to level 4
    def mature(self):
        pass

    #  :level 4 to level 5
    def ancient(self):
        pass

    # last level    :level 5 to level 6
    def snag(self):
        print('Snag')
    
