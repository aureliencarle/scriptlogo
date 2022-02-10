#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scriptsplash.utils import GlobalVariable

class Color:
    HEADER = '\033[95m'
    BLUE   = '\033[94m'
    CYAN   = '\033[96m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    RED    = '\033[91m'
    BOLD   = '\033[1m'
    ULINE  = '\033[4m'
    ENDC   = '\033[0m'


class String:
    text  = ''
    size  = 0

    def __init__(self, text, color = None):
        if text:
            self.text = text
            self.size = len(text)
        if color is not None:
            self.colored(color)
        else:
            pass

    def colored(self, color):
        if color is not None:
            self.text = color+self.text+Color.ENDC

    def underlined(self):
        self.text = Color.ULINE+self.text+Color.ENDC

class Log:
    '''
    '''
    @staticmethod
    def print(object) -> None:
        print(GlobalVariable.LOG_ALINEA+' PRINT   '+GlobalVariable.LOG_SYMBOL+' '+str(object))

    @staticmethod
    def debug(words) -> None:
        print(GlobalVariable.LOG_ALINEA+ Color.GREEN+' DEBUG   '+GlobalVariable.LOG_SYMBOL+' '+Color.ENDC+str(words))

    @staticmethod
    def info(words) -> None:
        print(GlobalVariable.LOG_ALINEA+ Color.CYAN+' INFO    '+GlobalVariable.LOG_SYMBOL+' '+Color.ENDC+str(words))

    @staticmethod
    def warning(words) -> None:
        print(GlobalVariable.LOG_ALINEA+ Color.YELLOW+' WARNING '+GlobalVariable.LOG_SYMBOL+' '+Color.ENDC+str(words))

    @staticmethod
    def error(words) -> None: 
        print(GlobalVariable.LOG_ALINEA+ Color.RED+' ERROR   '+GlobalVariable.LOG_SYMBOL+' '+Color.ENDC+str(words))
