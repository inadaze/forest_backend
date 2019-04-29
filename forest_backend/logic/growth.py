import json
import logging
import random
import requests
from forest_backend.logic.json_helper import JsonHelper
from forest_backend.logic.external_api_configs.oxford_dictionary import config
from forest_backend.logic.internal_api_configs.forest_backend import config as forest_config


LOGGER = logging.getLogger('forest_backend_scheduler')

class Growth(object):
    url = None
    forest_url = None
    headers = {'app_id': '53e47906', "app_key": "d469e72695b750d658d9289f7f580bfd"}
    json_helper = None

    def __init__(self):
        LOGGER.info('Starting Growth')
        self.url = config['url']
        self.forest_url = forest_config['url']
        self.forest_headers = forest_config['headers']
        self.json_helper = JsonHelper()
        print('Growth')

    # grow a seed into a new tree
    def germinate(self):
        LOGGER.info('Running Germinate')
        get_seeds_url = self.forest_url + "seeds/" + 'new'
        new_seeds_resp = requests.get(get_seeds_url, headers=self.forest_headers)
        new_seeds = new_seeds_resp.json()
        LOGGER.info('Found %s new seeds', len(new_seeds['data']))

        for seed in new_seeds['data']:
            put_tree_url = self.forest_url + "tree/" + seed['word']
            status = requests.put(put_tree_url, headers=self.forest_headers).status_code
            if status != 204:
                LOGGER.warning('Seed with the word %s did not germinate into a tree', seed['word'])
        return True

    # first level level 0 to level 1
    def sprout(self):
        get_trees_url = self.forest_url + "trees"
        new_trees_resp = requests.get(
            get_trees_url,
            data=json.dumps({"level_id": 0}),
            headers=self.forest_headers
            )
        new_trees = new_trees_resp.json()

        for tree in new_trees['data']:
            update_tree_level = False
            synonym_url = self.url + tree['seed']['word'] + "/synonyms"

            get_synonym_resp = requests.get(synonym_url, headers=self.headers)
            if get_synonym_resp.status_code == 200:
                
                json_data = get_synonym_resp.json()
                synonyms = self.json_helper.get_synonyms(json_data)

                chosen_synonyms = random.sample(synonyms, 3)
                for synonym in chosen_synonyms:
                    put_branch_url = self.forest_url + 'branch'
                    new_branch = requests.put(
                        put_branch_url,
                        data=json.dumps({"tree_id": tree['id'], "idea": synonym}),
                        headers=self.forest_headers
                        )
                    if new_branch.status_code != 204:
                        LOGGER.warning(
                            "Could not create branch with idea %s on tree %s", synonym, tree['id']
                            )
                    else:
                        update_tree_level = True

                if update_tree_level:
                    update_tree_url = self.forest_url + 'tree'
                    update_tree = requests.patch(
                        update_tree_url,
                        data=json.dumps({"id": tree['id'], 'level_id': 1}),
                        headers=self.forest_headers
                        )
                    if update_tree.status_code != 200:
                        LOGGER.error('Was not able to update tree with id %s to a sprout', tree['id'])
            else:
                LOGGER.error('Could not get a synonym for the word %s for tree %s', tree['seed']['word'], tree['id'])

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
    
