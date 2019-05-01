""" Module of helper functions for supporting the logic subpackage """

class JsonHelper():
    """ Helper functions for parsing external api responses """
    def __init__(self):
        pass

    def get_synonyms(self, json_data):
        """ Return all the synonyms from the response from Oxford Thesaurus """
        json_synonyms = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        synonyms = []
        for synonym in json_synonyms:
            synonyms.append(synonym['text'])

        return synonyms
