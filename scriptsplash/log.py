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

from scriptsplash.utils import GlobalVariable
from colorama import Fore, Back, Style


class Color:
    # Color
    BLACK = '\033[30m'
    WHITE = '\033[97m'
    DARKGRAY = '\033[90m'
    DARKRED = '\033[31m'
    DARKGREEN = '\033[32m'
    DARKYELLOW = '\033[33m'
    DARKBLUE = '\033[34m'
    DARKMAGENTA = '\033[35m'
    DARKCYAN = '\033[36m'
    GRAY = '\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BLACK_BACKGROUND = '\033[40m'
    WHITE_BACKGROUND = '\033[107m'
    DARKRED_BACKGROUND = '\033[41m'
    DARKGREEN_BACKGROUND = '\033[42m'
    DARKYELLOW_BACKGROUND = '\033[43m'
    DARKBLUE_BACKGROUND = '\033[44m'
    DARKMAGENTA_BACKGROUND = '\033[45m'
    DARKCYAN_BACKGROUND = '\033[46m'
    DARKGRAY_BACKGROUND = '\033[100m'
    GRAY_BACKGROUND = '\033[47m'
    RED_BACKGROUND = '\033[101m'
    GREEN_BACKGROUND = '\033[102m'
    YELLOW_BACKGROUND = '\033[103m'
    BLUE_BACKGROUND = '\033[104m'
    MAGENTA_BACKGROUND = '\033[105m'
    CYAN_BACKGROUND = '\033[106m'
    # Char stats
    BOLD = '\033[1m'
    ULINE = '\033[4m'
    ENDC = '\033[0m'


class Format:
    @staticmethod
    def styled(
        text: str, color: str, style: str = 'normal', backgroud=None
    ) -> str:
        """Apply color special characters to a string"""
        color_str = getattr(Fore, color.upper())
        backg_str = ''
        if backgroud is not None:
            backg_str = getattr(Back, backgroud.upper())
        style_str = getattr(Style, style.upper())
        reset_str = Style.RESET_ALL
        return f'{color_str}{style_str}{backg_str}{text}{reset_str}'

    @staticmethod
    def styled_log(
        alinea: str, color: str, log: str, symbol: str, object: any
    ) -> None:
        color_str = getattr(Fore, color.upper())
        reset_str = Style.RESET_ALL
        return f'{alinea}{color_str}{log}{symbol}{reset_str}{str(object)}'


class String:
    text = ''
    size = 0

    def __init__(self, text, color=None):
        if text:
            self.text = text
            self.size = len(text)
        if color is not None:
            self.colored(color)
        else:
            pass

    def colored(self, color, background=None):
        if color is not None:
            self.text = Format.styled(self.text, color)


class Log:
    ''' '''

    @staticmethod
    def general_print(alinea, color, log, symbol, object):
        print(Format.styled_log(alinea, color, log, symbol, object))

    @staticmethod
    def print(object) -> None:
        Log.general_print(
            GlobalVariable.LOG_ALINEA,
            'reset',
            ' PRINT   ',
            GlobalVariable.LOG_SYMBOL,
            str(object),
        )

    @staticmethod
    def debug(words) -> None:
        Log.general_print(
            GlobalVariable.LOG_ALINEA,
            'green',
            ' DEBUG   ',
            GlobalVariable.LOG_SYMBOL,
            str(words),
        )

    @staticmethod
    def info(words) -> None:
        Log.general_print(
            GlobalVariable.LOG_ALINEA,
            'cyan',
            ' INFO    ',
            GlobalVariable.LOG_SYMBOL,
            str(words),
        )

    @staticmethod
    def warning(words) -> None:
        Log.general_print(
            GlobalVariable.LOG_ALINEA,
            'yellow',
            ' WARNING ',
            GlobalVariable.LOG_SYMBOL,
            str(words),
        )

    @staticmethod
    def error(words) -> None:
        Log.general_print(
            GlobalVariable.LOG_ALINEA,
            'red',
            ' ERROR   ',
            GlobalVariable.LOG_SYMBOL,
            str(words),
        )
