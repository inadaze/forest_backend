

class JsonHelper():

    def __init__(self):
        pass

    def get_synonyms(self, json_data):
        json_synonyms = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        synonyms = []
        for synonym in json_synonyms:
            synonyms.append(synonym['text'])

        return synonyms
