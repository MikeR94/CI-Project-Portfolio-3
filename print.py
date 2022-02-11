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


def formula_1_text():
    """ Prints formula 1 in ASCI text"""
    red_string('''             ___________                         __            ____
             \_   _____/__________  _____  __ __|  | _____    /_   |
              |    __)/  _ \_  __ \/     \|  |  \  | \__  \    |   |
              |     \(  <_> )  | \/  Y Y  \  |  /  |__/ __ \_  |   |
              \___  / \____/|__|  |__|_|  /____/|____(____  /  |___|
                  \/                    \/                \/        \n''')


def multiple_blank_lines():
    """ Used to call blank_lines() multiple times and not clutter run.py"""
    blank_line()
    blank_line()
    blank_line()
    blank_line()
    blank_line()


def solid_line(new_line_at_end=False):
    """ Prints a solid line the length of the terminal"""
    if new_line_at_end:
        print('\u001b[31m======================'
        '================================='
        '=========================\u001b[0m\n')
    else:
        print('\u001b[31m======================'
        '================================='
        '=========================\u001b[0m')


def blank_line():
    """ Prints a blank line to the terminal """
    print()


def red_string(text):
    """ Print a string in the colour red """
    string = f"\033[31;1m{text}\033[0m"
    print(string)


def green_string(text):
    """ Print a string in the colour green """
    string = f"\033[32;1m{text}\033[0m"
    print(string)


def yellow_string(text):
    """ Print a string in the colour yellow """
    string = f"\033[33;1m{text}\033[0m"
    print(string)


def blue_string(text):
    """ Print a string in the colour blue """
    string = f"\033[34;1m{text}\033[0m"
    print(string)


def magenta_string(text):
    """ Print a string in the colour magenta """
    string = f"\033[35;1m{text}\033[0m"
    print(string)


def cyan_string(text):
    """ Print a string in the colour cyan """
    string = f"\033[36;1m{text}\033[0m"
    print(string)


def white_string(text):
    """ Print a string in the colour white """
    string = f"\033[37;1m{text}\033[0m"
    print(string)
