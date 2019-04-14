import json
import requests
from forest_backend.scheduler.json_helper import JsonHelper
from forest_backend.scheduler.external_api_configs.oxford_dictionary import config

class Growth(object):
    url = None
    headers = {'app_id': '53e47906', "app_key": "d469e72695b750d658d9289f7f580bfd"}
    json_helper = None

    def __init__(self):
        self.url = config['url']
        self.json_helper = JsonHelper()
        print('Growth')

    # first level
    def sprout(self):
        synonym_url = self.url + "excellent" + "/synonyms"
        response = requests.get(synonym_url, headers=self.headers)
        json_data = json.loads(response.text)
        synonyms = self.json_helper.get_synonyms(json_data)
        print(synonyms)
        return synonyms

    # last level
    def snag(self):
        print('Snag')
