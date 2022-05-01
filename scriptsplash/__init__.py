#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Les imports réalisé ici facilite les imports dans les scripts:
    Au lieu de:
        from scriptsplash.splash import Splash
    faire:
        from scriptsplash import Splash
"""

name = "scriptsplash"

# Core of this module
from scriptsplash.splash import Splash
from scriptsplash.utils import GlobalVariable
from scriptsplash.log import Log

# Possibility if you want to use utils class (but too specific to be interesting)
from scriptsplash.log import String
from scriptsplash.utils import ASCII
