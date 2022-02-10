#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scriptsplash.splash import Splash
from scriptsplash.log    import Color, Log
from scriptsplash.utils import GlobalVariable

if __name__ == '__main__':

    #GlobalVariable.set(width = 100, log_symbol = '\u00bb')

    script_splash = Splash()
    script_splash.borders(color = Color.BLUE, font='ANSI Shadow')

    script_splash.add_empty_line()
    script_splash.add_ansi_logo(
        'The Logo', 
        align = 'center',
        color = Color.GREEN
    )
    script_splash.add_one_content_line(
        'by Arc-Pintade',  
        align  = 'right'
    )
    script_splash.add_empty_line()
    
    script_splash.add_separator()

    script_splash.add_two_content_line(
        'Welcome to THE PROGRAM', 'http://gitlab.com', 
        align  = 'middle',
        color1 = None,
        color2 = Color.CYAN
    )
    script_splash.add_one_content_line(
        '(c) 1992-2022, The Prog Team',  
        align  = 'right'
    )
    script_splash.add_one_content_line(
        'Built for linuxx8664gcc',   
        align  = 'left',
        color  = Color.RED
    )
    script_splash.add_one_content_line(
        'From tags/some_branch@v1.0', 
        align  = 'left'
    )
    script_splash.add_one_content_line(
        'Try \'.help\', \'.demo\', \'.license\', \'.credits\', \'.quit\'/\'.q\'',  
        align  = 'left'
    )

    script_splash.print_splash()


    Log.print({'a' : {'first' : 1, 'second' : 2}, 'b' : [1,2,3] , 'c' : None})
    Log.debug('this is : debug')
    Log.info('this is : info')
    Log.warning('this is : warning')
    Log.error('this is : error ')