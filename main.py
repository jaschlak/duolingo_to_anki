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
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    
    # get words from duo
    sel = SelObj()
    sel.login()
    sel.load_words()
    duo_list = sel.create_list()
    sel.close()
    
    # get cards from anki deck
    anki = AnkiObj()
    anki_list = anki.read_deck()
    
    
    # compare count and add newest words
    count_dif = len(duo_list) - len(anki_list)
    
    if count_dif == 0:
        print('No cards to import')
    
    for i in range(0,count_dif):
        
        anki.add_to_deck(duo_list[i]['front'],duo_list[i]['back'])
        print('adding card: {}'.format(duo_list[i]))
