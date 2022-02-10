#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scriptsplash.utils import ASCII, GlobalVariable
from scriptsplash.log import Log, String

align_options = ['center', 
                 'middle', 
                 'left',
                 'right'
                ]

class Canvas:
    '''
    '''
    global_color = None
    width = 0
    block = []

    def __init__(self, global_color):    
        self.width        = GlobalVariable.WIDTH
        self.global_color = global_color
        for a in ASCII.Frame.keys():
            if not a.startswith('__'):
                setattr(Canvas, a, String(''))

    def borders(self, color = None, font = 'ANSI Shadow'):
        if self.global_color is not None:
            color = self.global_color
        for a in ASCII.Frame.keys():
            if not a.startswith('__'):
                setattr(Canvas, a, String(ASCII.Frame[a][font], color))

    def empty_line(self):
        return ' '*self.width

    def horizontal_line(self, is_filled = True):
        if is_filled:
            return self.horizontal.text*self.width
        else:
            return self.horizontal.text + ' '*(self.width - 2) + self.horizontalh.text

    def separator(self, symbol = None):
        if symbol is not None:
            return self.v.text + symbol*(self.width - 2) + self.v.text
        else:
            return self.center_left.text + self.horizontal.text*(self.width - 2) + self.center_right.text

    def vertical_line(self, line1 = None, line2 = None, align = 'left') -> str:
        result = self.vertical.text
        offset = 1 
        if line1 is None and line2 is None:
            result += ' '*(self.width - 2)
        else:
            if line2 is None:
                line2 = String('')
            filled_space = self.width - line1.size - line2.size - 2 
            n_space_right  = filled_space - offset    # cosmetic shift -offset
            n_space_left   = offset                   # cosmetic shift +offset
            n_space_middle = 0
            if align is 'center' :
                n_space_left  = int(filled_space / 2)
                n_space_right = filled_space - n_space_left
            elif align is 'right':
                n_space_left = filled_space - offset
                n_space_right = offset
            elif align is 'middle':
                n_space_right  = offset 
                n_space_left   = offset
                n_space_middle = filled_space - 2*offset 

            result += ' '*n_space_left + line1.text + ' '*n_space_middle + line2.text+ ' '*n_space_right
        return result + self.vertical.text

    def top(self):
        return self.top_left.text + self.horizontal.text * (self.width - 2) + self.top_right.text

    def bottom(self):
        return self.bottom_left.text + self.horizontal.text * (self.width - 2) + self.bottom_right.text

    def wraped(self):
        result = [self.empty_line(), self.top()]
        for line in self.block:
            result.append(line)
        result.append(self.bottom())
        return result

    def print_splash(self) -> None:
        result = ''
        for l in self.wraped():
            result += l + '\n'
        print(result)

class Splash(Canvas):
    '''
    '''
    def __init__(self, global_color = None):
        super().__init__(global_color)

    def generate_ansi(self, text, font='ANSI Shadow', color = None):
        if self.global_color is not None:
            color = self.global_color
        result = []
        for char in text:
            if char.islower():
                try: 
                    ASCII.Font[font][char]
                except KeyError:
                    text = text.upper()
        for i in range(len(ASCII.Font[font]['A'])-1):
            line = ''
            for letter in text:
                if letter in ASCII.Forbidden[font]:
                    continue
                line += ASCII.Font[font][letter][i]
            string_line = String(line)
            string_line.colored(color)
            result.append(string_line)
        #if len(text)*ASCII.Font[font]['width'] >= 80:
        #    Log.warning('ANSI width bigger than canvas width')
        #    Log.info('change canvas width with 'GlobalVariable.set()'')
        return result


    def add_ansi_logo(self, logo, align = 'left', color = None):
        if self.global_color is not None:
            color = self.global_color
        for line in self.generate_ansi(logo, color = color):
            self.block.append(self.vertical_line(line, align=align))

    def add_empty_line(self):
        self.block.append(self.vertical_line())

    def add_separator(self, symbol = None):
        self.block.append(self.separator(symbol))

    def add_one_content_line(self, line, align = 'left', color = None):
        if self.global_color is not None:
            color = self.global_color
        if align in align_options:
            string = String(line)
            string.colored(color)
            self.block.append(self.vertical_line(string, align=align))
        else:
            Log.error('bad align option')

    def add_two_content_line(self, line1, line2, align = 'left', color1 = None, color2 = None):
        if self.global_color is not None:
            color1 = self.global_color
            color2 = self.global_color
        string1 = String(line1)
        string2 = String(line2)
        string1.colored(color1)
        string2.colored(color2)
        self.block.append(self.vertical_line(string1, string2, align=align))

