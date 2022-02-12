#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Copyright (C) La Labomedia August 2018
#
# This file is part of scriptsplash.

# scriptsplash is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# scriptsplash is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with scriptsplash.  If not, see <https://www.gnu.org/licenses/>.
#######################################################################

import argparse
from tkinter import font

from scriptsplash import Splash
from scriptsplash import Color, Log
#from scriptsplash.utils  import GlobalVariable

parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store_true', help='any argument')
parser.add_argument('-b', action='store', help='another argument')
parser.add_argument('-c', action='store', nargs="?", help='another argument again')
args = parser.parse_args()


import sys
if __name__ == '__main__':

    #GlobalVariable.set(width=100, log_symbol='\u00bb')

    splash1 = Splash()
    splash1.borders(color=Color.BLUE, font='ANSI Shadow')
    splash1.add_empty_line()

    splash1.add_ansi_logo(
        'Splash', 
        font='ANSI Shadow',
        align='center',
        color=Color.GREEN
    )
    splash1.add_one_content_line(
        'by Arc-Pintade',  
        align='right'
    )
    splash1.add_empty_line()
    
    splash1.add_separator()

    splash1.add_two_content_line(
        'Welcome to THE ScriptSplash program', 'http://github.com', 
        align='middle',
        color1=None,
        color2=Color.CYAN
    )
    splash1.add_one_content_line(
        'Aurélien Carle',  
        align='right'
    )
    splash1.add_one_content_line(
        'Built for linuxx8664gcc',   
        align='left',
        color=Color.RED
    )
    splash1.add_one_content_line(
        'From the only existing branch ... v1.0', 
        align='left',
        color=Color.DARKBLUE_BACKGROUND+Color.BLACK
    )
    splash1.add_separator(
        '-', 
        color=Color.YELLOW
    )
    splash1.add_argparse_help(
        parser,
        align='left',
        color=Color.YELLOW
    )

    splash1.print_splash()

    #########################################
    #########################################

    splash2 = Splash()
    splash2.add_ansi_logo(
        'HackerNoob', 
        font='ANSI Bloody',
        align='center',
        color=Color.DARKRED
    )
    splash2.print_splash()

    #########################################
    #########################################

    splash3 = Splash(global_color=Color.GREEN)
    splash3.borders(color=Color.BLUE, font='Minimal')
    splash3.add_two_content_line(
        'Welcome to THE ScriptSplash program', 'http://github.com', 
        align='middle',
        color1=None,
        color2=Color.CYAN
    )
    splash3.add_one_content_line(
        'Aurélien Carle',  
        align='right'
    )
    splash3.add_one_content_line(
        'Built for linuxx8664gcc',   
        align='left',
        color=Color.RED
    )
    splash3.add_one_content_line(
        'From the only existing branch ... v1.0', 
        align='left'
    )
    splash3.add_separator(
        '-', 
        color=Color.YELLOW
    )
    splash3.add_argparse_help(
        parser,
        align='left',
        color=Color.YELLOW
    )
    splash3.print_splash(lolcat=True)

    #########################################
    #########################################

    Log.print({'a' : {'first' : 1, 'second' : 2}, 'b' : [1,2,3] , 'c' : None})
    Log.debug('this is : debug')
    Log.info('this is : info')
    Log.warning('this is : warning')
    Log.error('this is : error ')

