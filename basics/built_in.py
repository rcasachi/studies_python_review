pow(2, 3) # base**exp

dir(__builtins__) # All builtin functions

help(max) # Help about a functionality of any function

import math
math.sqrt(16) # square root

dir(math) # know all the functions in a module

math.__doc__ # Documentation about module and functions at math

"""This is the module docstring"""

def sayHello():
    """This is the function docstring"""
    return 'Hello World'

sayHello.__doc__