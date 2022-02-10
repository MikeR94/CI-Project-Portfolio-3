""" File used to prepare different coloured strings """

import colorama

colorama.init()

"""
Black: \u001b[30m.
Red: \u001b[31m.
Green: \u001b[32m.
Yellow: \u001b[33m.
Blue: \u001b[34m.
Magenta: \u001b[35m.
Cyan: \u001b[36m.
White: \u001b[37m.
"""


def red_string(text):
    """ Print a string in the colour red """
    string = f"\033[31;1m{text}\033[0m"
    print(string)
