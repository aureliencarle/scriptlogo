#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyrfc3339 import generate
from scriptlogo.fonts import ASCII

SIZE = 80

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


align_options = ["center", 
                 "middle", 
                 "left",
                 "right"
                ]

class String:
    text  = ""
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


class Canvas:
    """
    """
    color = None
    size  = SIZE
    block = []

    def __init__(self):    
        for a in ASCII.Frame.keys():
            if not a.startswith("__"):
                setattr(Canvas, a, String(""))

    def new_canvas(self, color = None, font = "ANSI Shadow"):
        for a in ASCII.Frame.keys():
            if not a.startswith("__"):
                setattr(Canvas, a, String(ASCII.Frame[a][font], color))

    def empty_line(self):
        return ' '*self.size

    def horizontal_line(self, is_filled = True):
        if is_filled:
            return self.horizontal.text*self.size
        else:
            return self.horizontal.text + ' '*(self.size - 2) + self.horizontalh.text

    def separator(self, symbol = None):
        if symbol is not None:
            return self.v.text + symbol*(self.size - 2) + self.v.text
        else:
            return self.center_left.text + self.horizontal.text*(self.size - 2) + self.center_right.text

    def vertical_line(self, line1 = None, line2 = None, align = "left") -> str:
        result = self.vertical.text
        offset = 1 

        if line1 is None and line2 is None:
            result += ' '*(self.size - 2)
        else:
            if line2 is None:
                line2 = String("")
            filled_space = self.size - line1.size - line2.size - 2 
            n_space_right  = filled_space - offset    # cosmetic shift -offset
            n_space_left   = offset                   # cosmetic shift +offset
            n_space_middle = 0
            if align is "center" :
                n_space_left  = int(filled_space / 2)
                n_space_right = filled_space - n_space_left
            elif align is "right":
                n_space_left = filled_space - offset
                n_space_right = offset
            elif align is "middle":
                n_space_right  = offset 
                n_space_left   = offset
                n_space_middle = filled_space - 2*offset 

            result += ' '*n_space_left + line1.text + ' '*n_space_middle + line2.text+ ' '*n_space_right
        return result + self.vertical.text

    def up(self):
        return self.top_left.text + self.horizontal.text * (self.size - 2) + self.top_right.text

    def down(self):
        return self.bottom_left.text + self.horizontal.text * (self.size - 2) + self.bottom_right.text

    def wrap(self):
        result = [self.empty_line(), self.up()]
        for line in self.block:
            result.append(line)
        result.append(self.down())
        return result

    def get_canvas(self) -> str:
        result = ''
        for l in self.wrap():
            result += l + '\n'
        return result


class Logo(Canvas):
    """
    """
    def __init__(self):
        Canvas().__init__()

    def generate_ansi(self, logo, font='ANSI Shadow', color = None):
        result = []
        for char in logo:
            if char.islower():
                try: 
                    ASCII.Font[font][char]
                    #fonts.font_list[font][0][char]
                except KeyError:
                    logo = logo.upper()
        for i in range(len(ASCII.Font[font]['A'])-1):
            line = ""
            for letter in logo:
                if letter in ASCII.Forbidden[font]:
                    continue
                line += ASCII.Font[font][letter][i]
            string_line = String(line)
            string_line.colored(color)
            result.append(string_line)
        return result


    def add_ansi_logo(self, logo, align = "left", color = None):
        for line in self.generate_ansi(logo, color = color):
            self.block.append(self.vertical_line(line, align=align))

    def add_empty_line(self):
        self.block.append(self.vertical_line())

    def add_separator(self, symbol = None):
        self.block.append(self.separator(symbol))

    def add_one_content_line(self, line, align = "left", color = None):
        if align in align_options:
            string = String(line)
            string.colored(color)
            self.block.append(self.vertical_line(string, align=align))
        else:
            print("error")

    def add_two_content_line(self, line1, line2, align = "left", color1 = None, color2 = None):
        string1 = String(line1)
        string2 = String(line2)
        string1.colored(color1)
        string2.colored(color2)
        self.block.append(self.vertical_line(string1, string2, align=align))

    def update(self):
        self.block = self.generate_block()

