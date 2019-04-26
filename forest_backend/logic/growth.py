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
        self.forest_url = forest_config['url']
        self.forest_headers = forest_config['headers']
        self.json_helper = JsonHelper()
        print('Growth')

    # grow a seed into a tree : level 0 to level 1
    def germinate(self):
        get_seeds_url = self.forest_url + "seeds"
        new_seeds = requests.get(get_seeds_url, headers=self.forest_headers).json()

        for seed in new_seeds['data']:
            put_tree_url = self.forest_url + "tree/" + seed['word']
            status = requests.get(put_tree_url, headers=self.forest_headers).status_code
            if status != 204:
                # TODO: create logger saying there is a missed seed
                pass
        return True

    # first level level 1 to level 2
    def sprout(self):
        #TODO: fetch all new seeds and turn into sprouts
        get_seeds_url = self.forest_url + "seeds"
        data = {"tree_level": 0}
        new_seeds = requests.get(get_seeds_url, data=json.dumps(data), headers=self.forest_headers)
        synonym_url = self.url + "excellent" + "/synonyms"

        response = requests.get(synonym_url, headers=self.headers)
        json_data = json.loads(response.text)
        synonyms = self.json_helper.get_synonyms(json_data)
        print(synonyms)
        return synonyms

    #  :level 2 to level 3
    def seedling(self):
        pass

    #  :level 3 to level 4
    def sapling(self):
        pass

    #  :level 4 to level 5
    def mature(self):
        pass

    #  :level 6 to level 7
    def ancient(self):
        pass

    # last level    :level 7 to level 8
    def snag(self):
        print('Snag')
    
