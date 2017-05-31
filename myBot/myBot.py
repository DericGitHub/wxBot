#!/usr/bin/python
from wxbot import *
import ConfigParser
import json

'''
Feature list:

1. If got a candidate requirement message,check with the submitter.
2. Check in
'''
'''
Switch status
'''
OFF = 0
ON = 1
points = 500
HOME_PAGE = 'your points is %d'
class myWXBot(WXBot):
    '''
    Public method
    '''
    def __init__(self):
        self.switch_for_all = ON
        self.home_page = HOME_PAGE
        try:
            cf = ConfigParser.ConfigParser()
            cf.read('UserInterface.ini')
            
    def shutdown_controlled(self):
        pass
    def shutdown_immediate(self):
        pass
    def query(self):
        pass
    def server_configure(self):
        pass
    def set_config_parameter(self):
        pass
    def handle_msg_all(self,msg):
    
    '''
    Private method
    '''
    def _reload(self):
        pass
    def _reset(self):
        pass
    def _display_home_page(self):
        msg = ''
        return msg % (points)



        
        

