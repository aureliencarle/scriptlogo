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

    script_splash = Splash()
    script_splash.borders(color=Color.BLUE, font='ANSI Shadow')
    script_splash.add_empty_line()

    script_splash.add_ansi_logo(
        'Splash', 
        align='center',
        color=Color.GREEN
    )
    script_splash.add_one_content_line(
        'by Arc-Pintade',  
        align='right'
    )
    script_splash.add_empty_line()
    
    script_splash.add_separator()

    script_splash.add_two_content_line(
        'Welcome to THE ScriptSplash program', 'http://github.com', 
        align='middle',
        color1=None,
        color2=Color.CYAN
    )
    script_splash.add_one_content_line(
        'Aurélien Carle',  
        align='right'
    )
    script_splash.add_one_content_line(
        'Built for linuxx8664gcc',   
        align='left',
        color=Color.RED
    )
    script_splash.add_one_content_line(
        'From the only existing branch ... v1.0', 
        align='left'
    )
    script_splash.add_separator(
        '-', 
        color=Color.YELLOW
    )
    script_splash.add_argparse_help(
        parser,
        align='left',
        color=Color.YELLOW
    )

    script_splash.print_splash()


    Log.print({'a' : {'first' : 1, 'second' : 2}, 'b' : [1,2,3] , 'c' : None})
    Log.debug('this is : debug')
    Log.info('this is : info')
    Log.warning('this is : warning')
    Log.error('this is : error ')

