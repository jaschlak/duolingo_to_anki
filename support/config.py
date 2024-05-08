# -*- coding: utf-8 -*-

import json

def get_configuration(filepath='input/config.json'):    
    
    try:
        f = open(filepath)
        
        return json.load(f)
    
    except Exception as e:
        
        print('Could not find config file at {}, error: {}'.format(filepath,e))