import time
import requests
import json
from forest_backend.scheduler.json_helper import JsonHelper

class Growth(object): 
    url = 'https://od-api.oxforddictionaries.com/api/v1/entries/en/excellent/synonyms'

    def __init__(self):
        print('Growth')

    # first level
    def sprout(self):
        headers = {'app_id': '53e47906', "app_key": "d469e72695b750d658d9289f7f580bfd"}
        response = requests.get(self.url, headers=headers)
        json_data = json.loads(response.text)
        json_helper = JsonHelper()
        synonyms = json_helper.get_synonyms(json_data)
        print('Sprout')
        print(synonyms)

    # last level
    def snag(self):
        print('Snag')
