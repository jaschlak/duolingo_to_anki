# -*- coding: utf-8 -*-

import requests
import json

from support.config import get_configuration

class AnkiObj:
    
    def __init__(self):
        
        config = get_configuration()['anki']
        
        self.url = config['url']
        self.deckname = config['deckname']
        self.tags = config['tags']
        
    def get_card_ids(self):
        
        request = {
            "action": "findCards",
            "version": 6,
            "params": {
                "query": "deck:{}".format(self.deckname)
            }
        }
        
        response = requests.post(self.url, json=request)
        
        if response.ok:
            return  response.json()['result']
        else:
            print('problem retrieving card ids from anki')
        
    def read_deck(self):
        
        card_id_list = self.get_card_ids()
            
        request = {
            "action": "cardsInfo",
            "version": 6,
            "params": {
                "cards": card_id_list
            }
        }
        
        response = requests.post(self.url, json=request)
        
        if response.ok:
            return response.json()['result']
        else:
            print('problem retrieving cards with card ids')
            
    
        
    def add_to_deck(self,front,back):
        
        # Custom note data
        note_data = {
            'deckName': self.deckname,
            'modelName': 'Basic',
            'fields': {
                'Front': front,
                'Back': back
            },
            'options': {
                'allowDuplicate': False
            },
            'tags': ['Duolingo', 'Japanese', 'N5']
        }
        
        # AnkiConnect addNote action
        add_note_action = {
            'action': 'addNote',
            'params': {
                'note': note_data
            }
        }
        
        
        
        # Send POST request to AnkiConnect
        response = requests.post(self.url, data=json.dumps(add_note_action))
        
        # Check if the request was successful
        if response.status_code == 200:
            print('Note added successfully!')
        else:
            print('Failed to add note:', response.text)
            
if __name__ == '__main__':
    
    anki = AnkiObj()
    
    test = anki.read_deck()