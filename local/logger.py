import logging
from logging.handlers import TimedRotatingFileHandler
import sys

class __AppLogger:
    def __init__(self, name, level=logging.INFO, enable_file_logging=False):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(level)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M')
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.__logger.addHandler(console_handler)
        
        if enable_file_logging:
            file_handler = TimedRotatingFileHandler('log', when='midnight', interval=1, backupCount=5)
            file_handler.setFormatter(formatter)
            self.__logger.addHandler(file_handler)
    
    def get_logger(self):
        return self.__logger
    
APP_LOGGER = __AppLogger('app', enable_file_logging=True).get_logger()