# -*- coding: utf-8 -*-

import os
import logging
from logging import handlers

from support.config import get_configuration
config = get_configuration()

class LogClass:
   
    def __init__(self):
       
        self.logger = logging.getLogger()
        self.level = logging.INFO
       
        filename = config['project_name'] + '.log'
       
        if os.name == 'nt':
            folderpath = './output'
        elif os.name == 'posix':
            folderpath = './output'
        else:
            folderpath = '~'
            filename = 'couldnt_detect_os.log'
           
        LOGFILEPATH = '/'.join([folderpath,filename])
       
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
       
        self.set_log_settings()
        self.set_log_directory(LOGFILEPATH)
       
    def set_log_settings(self):
       
        self.logger.setLevel(self.level)
       
    def set_log_directory(self, LOGFILEPATH):
       
        # important, handlers are global, this gets rid of old handlers
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)
       
        handler = logging.handlers.RotatingFileHandler(LOGFILEPATH, maxBytes=100000000, backupCount=20, encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(handler)