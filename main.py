# -*- coding: utf-8 -*-


'''
Make sure you copy the input/example_conf.json -> input/conf.json

This requires you have anki and install AnkiConnect (listens on port while open)

Install AnkiConnect Add-on:
    Open Anki.
    Go to Tools > Add-ons > Get Add-ons.
    Enter the code for AnkiConnect (2055492159) and install it.

'''

from support.selenium_module import SelObj
from support.anki_module import AnkiObj
from support.log import LogClass
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    
    log = LogClass()
    
    # get words from duo
    sel = SelObj()
    sel.login()
    sel.load_words()
    duo_list = sel.create_list()
    sel.close()
    
    # get cards from anki deck
    anki = AnkiObj()
    anki_list = anki.read_deck()
    
    # add card to deck if not already present
    for duo_item in duo_list:
        
        found = 0
        for anki_item in anki_list:
            
            if duo_item['front'] == anki_item['fields']['Front']['value']:
                found=1
                
        if not found:
            log.logger.info('adding card {} to deck'.format(duo_item['front']))
            anki.add_to_deck(duo_item['front'],duo_item['back'])
        else:
            log.logger.debug('{} already found in deck'.format(duo_item['front']))
    
    