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
