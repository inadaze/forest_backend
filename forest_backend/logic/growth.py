import json
import logging
import random
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
        logger.info('Starting Growth')
        self.url = config['url']
        self.forest_url = forest_config['url']
        self.forest_headers = forest_config['headers']
        self.json_helper = JsonHelper()
        print('Growth')

    # grow a seed into a new tree
    def germinate(self):
        logger.info('Running Germinate')
        get_seeds_url = self.forest_url + "seeds"
        new_seeds = requests.get(get_seeds_url, data=json.dumps({"tree_level": 0}), headers=self.forest_headers).json()
        logger.info('Found %s new seeds', len(new_seeds['data']))

        for seed in new_seeds['data']:
            put_tree_url = self.forest_url + "tree/" + seed['word']
            status = requests.put(put_tree_url, headers=self.forest_headers).status_code
            if status != 204:
                logger.warning('Seed with the word %s did not germinate into a tree', seed['word'])
        return True

    # first level level 0 to level 1
    def sprout(self):
        get_trees_url = self.forest_url + "trees"
        new_trees = requests.get(get_trees_url, data=json.dumps({"tree_level": 0}), headers=self.forest_headers).json()

        for tree in new_trees['data']:
            synonym_url = self.url + tree['seed']['word'] + "/synonyms"

            json_data = requests.get(synonym_url, headers=self.headers).json()
            synonyms = self.json_helper.get_synonyms(json_data)

            chosen_synonyms = random.sample(synonyms, 3)
            for synonym in chosen_synonyms:
                put_branch_url = self.forest_url + "branch"
                # TODO: create branches for tree,  increase tree_level
                new_branch = requests.get(put_branch_url, data=json.dumps({"tree_level": 0}), headers=self.forest_headers).json()


            print(synonyms)

        return True

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
    
