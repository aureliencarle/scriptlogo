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
    width = None
    block = None

    def __init__(self, global_color):
        self.block        = []
        self.width        = GlobalVariable.WIDTH
        self.global_color = global_color
        for a in ASCII.Frame.keys():
            if not a.startswith('__'):
                setattr(Canvas, a, String(''))

    def borders(self, color=None, font='ANSI Shadow'):
        if self.global_color is not None : color = self.global_color
        for a in ASCII.Frame.keys():
            if not a.startswith('__'):
                setattr(Canvas, a, String(ASCII.Frame[a][font], color))

    def empty_line(self):
        return ' '*self.width

    def horizontal_line(self, is_filled=True):
        if is_filled:
            return self.horizontal.text*self.width
        else:
            return self.horizontal.text + ' '*(self.width - 2) + self.horizontalh.text

    def separator(self, symbol=None, color=None):
        symbol_string = String(symbol, color)
        if symbol is not None:
            return self.vertical.text + symbol_string.text*(self.width - 2) + self.vertical.text
        else:
            return self.center_left.text + self.horizontal.text*(self.width - 2) + self.center_right.text

    def vertical_line(self, line1=None, line2=None, align='left') -> str:
        result = self.vertical.text
        offset = 1 
        if line1 is None and line2 is None:
            result += ' '*(self.width - 2)
        else:
            if line2 is None:
                line2 = String('')
            filled_space   = self.width - line1.size - line2.size - 2 
            n_space_right  = filled_space - offset    # cosmetic shift -offset
            n_space_left   = offset                   # cosmetic shift +offset
            n_space_middle = 0
            if align == 'center' :
                n_space_left  = int(filled_space / 2)
                n_space_right = filled_space - n_space_left
            elif align == 'right':
                n_space_left = filled_space - offset
                n_space_right = offset
            elif align == 'middle':
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

    def generate_string(self) -> str:
        result = ''
        for l in self.wraped():
            result += l + '\n'
        return result

    def print_splash(self) -> None:
        print(self.generate_string())

    # Not really useful except for debug
    def print_splash_as_cpp_function(self) -> None:
        print(self.splash_cpp())

    def export_to_cpp_file(self, filename):
        with open(filename, 'w') as cppFile:
            cppFile.write(self.splash_cpp())

    def splash_cpp(self):
        result  = '#include <string>\n\n'
        result += '// generate from scriptslash \n'
        result += '// check https://github.com/aureliencarle/scriptsplash.git \n'
        result += 'std::string splashFromPythonToCpp()\n'
        result += '{\n'
        result += '    std::string splash = "'+repr(self.generate_string())[1:-1]+'";\n'
        result += '    return splash;\n'
        result += '}\n'
        return result


class Splash(Canvas):
    '''
    '''
    def __init__(self, global_color=None):
        super().__init__(global_color)

    def generate_ansi(self, text, font, color):
        if self.global_color is not None : color = self.global_color
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

    def add_multi_line(self, multiline, align='left'):
        for line in multiline:
            self.block.append(self.vertical_line(line, align=align)) 

    def add_ansi_logo(self, logo, font='ANSI Shadow', align='left', color=None):
        self.add_multi_line(self.generate_ansi(logo, font, color=color), align=align)

    def add_empty_line(self):
        self.block.append(self.vertical_line())

    def add_separator(self, symbol=None, color=None):
        if self.global_color is not None:
            color = self.global_color
        self.block.append(self.separator(symbol, color))

    def add_one_content_line(self, line, align='left', color=None):
        if self.global_color is not None : color = self.global_color
        if align in align_options:
            string = String(line)
            string.colored(color)
            self.block.append(self.vertical_line(string, align=align))
        else:
            Log.error('bad align option')

    def add_two_content_line(self, line1, line2, align='left', color1=None, color2=None):
        if self.global_color is not None:
            color1 = self.global_color
            color2 = self.global_color
        string1 = String(line1)
        string2 = String(line2)
        string1.colored(color1)
        string2.colored(color2)
        self.block.append(self.vertical_line(string1, string2, align=align))

    def add_argparse_help(self, parser, align='left', color=None):
        if self.global_color is not None: 
            color=self.global_color
        help = []
        for line in parser.format_help().split('\n'):
            if line != '':
                help.append(String(line, color))
        self.add_multi_line(help)    

