#### Installation

* (Hugely) Inspired by [Créer son propre package python](https://ressources.labomedia.org/creer_son_propre_package_python)

~~~text
pip3 install -e git+https://github.com/aureliencarle/scriptsplash.git#egg=scriptsplash
~~~

Update:

~~~text
pip3 install --upgrade git+https://github.com/aureliencarle/scriptsplash.git#egg=scriptsplash
~~~

with this installation method a src directory will be created in your project directory with all the good ready-to-use settings and path

### How to use scriptsplash

Example of script :

~~~python
# Imports en python3
from scriptsplash import Logo
from scriptsplash import Color, Log
#from scriptsplash  import GlobalVariable

if __name__ == '__main__':

    try :
        # If needed change global variable first to store width of canvas and symbols for log print.
        # If not call GlobalVariable is declared with default value width=80 (unix convention).
        #GlobalVariable.set(width = 100, log_symbol = '\u00bb').

        # Create a splash context. A color can be given as argument for constructeur.
        # This parameter is global color that will override every other color.  
        script_splash = Splash()
        #script_splash = Splash(global_color = Color.Yellow)


        # Change font and color of the binding ('ANSI Shadow', 'Sharp'(#), 'Minimal'(- and |) ).
        script_splash.borders(color = Color.BLUE, font='Sharp')

        script_splash.add_empty_line()
        # ANSI logo :) Be careful ANSI letters are huge, can overflow the canvas and it's ugly.
        # The alignement, can be 'left', 'right', 'center'.
        # Their is a 'middle' alignement for line with two infos (see below).
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

        # If you want two informations on same line, each one have their own color variable.
        script_splash.add_two_content_line(
            'Welcome to THE ScriptSplash program', 'http://github.com', 
            align  = 'middle',
            color1 = None,
            color2 = Color.CYAN
        )
        script_splash.add_one_content_line(
            'Aurélien Carle',  
            align  = 'right'
        )
        script_splash.add_one_content_line(
            'Built for linuxx8664gcc',   
            align  = 'left',
            color  = Color.RED
        )
        script_splash.add_one_content_line(
            'From the only existing branch ... v1.0', 
            align  = 'left'
        )

        # Finaly print the splash.
        script_splash.print_splash()

        # Demo of very light Log class of scrpitsplash (can be useful).
        Log.print({'a' : {'first' : 1, 'second' : 2}, 'b' : [1,2,3] , 'c' : None})
        Log.debug('this is : debug')
        Log.info('this is : info')
        Log.warning('this is : warning')
        Log.error('this is : error ')

    except (KeyboardInterrupt, EOFError):
        print()
        Log.info("Keyboard interrupt")

~~~

### Licence

All scripts are under license : GNU GENERAL PUBLIC LICENSE Version 3
