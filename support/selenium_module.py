# -*- coding: utf-8 -*-

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

import time

from support.config import get_configuration

class SelObj:
    
    def __init__(self):
        
        self.config = get_configuration()['duolingo']
        
        self.email = self.config['email']
        self.password = self.config['password']
        
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        
        self.actions = ActionChains(self.driver)
        
    def login(self):
        
        self.driver.get('https://www.duolingo.com/practice-hub/words');
        
        self.driver.find_element(By.ID, 'web-ui1').send_keys(self.email)
        self.driver.find_element(By.ID, 'web-ui2').send_keys(self.password)
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='LOG IN']"))).click()
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div/div/div[3]//a[@href='/learn']")))
        
    def load_words(self):
        
        self.driver.get('https://www.duolingo.com/practice-hub/words')
        
        element = wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@role='button']")))
        
        while element:
        
            try:
                element.click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                
            except WebDriverException:
                log.logger.error("Element is not clickable")
                break
            
    def create_list(self):
        
        self.driver.execute_script("window.scrollTo(0, 0);")
        sitelist = wait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//section/ul")))

        li_elements  = sitelist.find_elements(By.XPATH, "./li")
        
        full_list=[]
        for li in li_elements:
            
            front = li.find_element(By.XPATH, "./div/div/div/h3").text
            back = li.find_element(By.XPATH, "./div/div/div/p").text
            
            full_list.append({'front':front,'back':back})
            
        return full_list
        
    def close(self):
        
        self.driver.close()
        
        
if __name__ == '__main__':
    
    sel = SelObj() 
    #config = get_configuration()