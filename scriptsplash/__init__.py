#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
    Ce module propose les outils les plus courrant que j'utilise,
    et aussi pour retrouver des syntaxes peu utilisée que je n'ai pas en mémoire,
    et qui nécessiteraient des recherches.
    Les imports réalisé ici facilite les imports dans les scripts:
    Au lieu de:
        from scriptlogo.shell_logo import Logo
    faire:
        from scriptlogo import Logo
"""

name = "scriptlogo"

# Core of this module
from scriptsplash.splash import Splash
from scriptsplash.utils  import GlobalVariable
from scriptsplash.log    import Log

# Possibility if you want to use utils class (but too specific to be interesting)
from scriptsplash.log    import Color
from scriptsplash.log    import String
from scriptsplash.utils  import ASCII