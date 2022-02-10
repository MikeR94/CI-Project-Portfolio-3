import colorama

colorama.init()

def red_string(text):
    """ Print a string in the colour red """
    string = f"\033[31;1m{text}\033[0m"
    print(string)
