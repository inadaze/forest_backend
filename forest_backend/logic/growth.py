""" Module to contain the tasks to be run by the Scheduler """
import json
import logging
import random
import requests
from .json_helper import JsonHelper
from .external_api_configs.oxford_dictionary import config
from .internal_api_configs.forest_backend import config as forest_config


LOGGER = logging.getLogger('forest_backend_scheduler')

class Growth(object):
    """
    Actions to grow a tree from seed to snag

    This is where calls to external and internal apis are made
    """
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

    def germinate(self):
        """
        Grow a seed into a tree

        Returns
        -------
        bool
            Returns true if successfully exited
        """

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

    def sprout(self):
        """
        Grow a new tree into a sprout
        Updates tree level from 0 to 1
        Fetches word synonyms

        Returns
        -------
        int
            Description of return value

        """
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
                        LOGGER.error(
                            'Was not able to update tree with id %s to a sprout',
                            tree['id']
                            )
            else:
                # pylint: disable=C0301
                #TODO: implement an error table for trees with errors so we can avoid searching them again
                LOGGER.error(
                    'Could not get a synonym for the word %s for tree %s',
                    tree['seed']['word'],
                    tree['id']
                    )

        return True

    def seedling(self):
        """
        Grow a new sprout into a seedling
        Updates tree level from 1 to 2

        Returns
        -------
        int
            Description of return value

        """
        print('Seedling')

    def sapling(self):
        """
        Grow a new seedling into a sapling
        Updates tree level from 2 to 3

        Returns
        -------
        int
            Description of return value

        """
        print('Sapling')

    def mature(self):
        """
        Grow a new sapling into a mature tree
        Updates tree level from 3 to 4

        Returns
        -------
        int
            Description of return value

        """
        print('Mature')

    def ancient(self):
        """
        Grow a new mature tree into an ancient tree
        Updates tree level from 4 to 5

        Returns
        -------
        int
            Description of return value

        """
        print('Ancient')

    def snag(self):
        """
        Grow an ancient tree into a snag
        Updates tree level from 5 to 6

        Returns
        -------
        int
            Description of return value

        """
        print('Snag')
