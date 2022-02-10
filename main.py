#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scriptlogo.shell_logo import Logo, Color

if __name__ == "__main__":

    logo = Logo()
    logo.new_canvas(color =Color.BLUE)

    logo.add_empty_line()
    logo.add_ansi_logo(
        "The Logo", 
        align = "center",
        color = Color.GREEN
    )
    logo.add_one_content_line(
        "by Arc-Pintade",  
        align  = "right"
    )
    logo.add_empty_line()
    
    logo.add_separator()

    logo.add_two_content_line(
        "Welcome to THE PROGRAM", "http://gitlab.com", 
        align  = "middle",
        color1 = None,
        color2 = Color.CYAN
    )
    logo.add_one_content_line(
        "(c) 1992-2022, The Prog Team",  
        align  = "right"
    )
    logo.add_one_content_line(
        "Built for linuxx8664gcc",   
        align  = "left",
        color  = Color.RED
    )
    logo.add_one_content_line(
        "From tags/some_branch@v1.0", 
        align  = "left"
    )
    logo.add_one_content_line(
        "Try '.help', '.demo', '.license', '.credits', '.quit'/'.q'",  
        align  = "left"
    )

    print(logo.get_canvas())

