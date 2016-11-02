# coding: utf-8
"""
:Script:   inspect_demo.py
:Author:   Dan.Patterson@carleton.ca
:Modified: 2016-10-29
:Purpose:  demonstration of the inspect module
:Requires:
: - demo_def - a function included here to use for testing
:
:Documentation:
:
:  inspect.isfunction(demo_def)      # True    
:  inspect.getsourcelines(demo_def)  # returns source code for the script
:  inspect.findsource(demo_def)      # function script source
:  inspect.getdoc(demo_def)
:        'dummy...\n: Demonstrates retrieving and documenting module
:         and function info.\n:'
:  inspect.getsource(demo_def)       # 
:  inspect.ismodule(np)              # True
:  inspect.getsourcefile(demo_def)
:         .../Documents/Numpy_Scripts/inspect_demo.py'
:  inspect.getsource(art.info)       # get array tools info function code
:
:The function can also be used....
:  demo_def.__defaults__  # (None,)
:  demo_def.__dict__      # {} 
:  demo_def.__getattribute__('__name__')  # 'demo_def'
:  demo_def.__module__    # '__main__'
:  demo_def.__name__      # 'demo_def'
"""

import sys
import numpy as np
from textwrap import dedent
import inspect

script = sys.argv[0]  # a useful way to get a file's name


def get_modu(obj):
    """ """
    frmt = """
    :-----------------------------------------------------------------
    :Module: .... {} ....
    :------
    :File: ...... 
    {}\n
    :Docs:
    {}\n
    :Members:
    {}\n
    :Source code:
    {}
    :
    :-----------------------------------------------------------------
    """
    lines, line_num = inspect.getsourcelines(obj)
    memb = [i[0] for i in inspect.getmembers(obj)]
    code = "".join(["{:4d}  {}".format(idx, line)
                    for idx, line in enumerate(lines)])
    args = [obj.__name__, obj.__file__, obj.__doc__, memb, code]        
    mod_mem = dedent(frmt).format(*args)
    return mod_mem


def get_func(obj, verbose=True):
    """ """
    frmt = """
    :-----------------------------------------------------------------
    :Function: .... {} ....
    :Line number... {}
    :Docs:
    {}
    :Defaults: {}
    :Keyword Defaults: {}
    :Variable names: {}
    :Source code:
    {}
    :
    :-----------------------------------------------------------------
    """
    import inspect
    lines, ln_num = inspect.getsourcelines(obj)
    code = "".join(["{:4d}  {}".format(idx, line)
                    for idx, line in enumerate(lines)])
    #vars = 
    args = [obj.__name__, ln_num, obj.__doc__, obj.__defaults__,
            obj.__kwdefaults__, obj.__code__.co_varnames, code]        
    code_mem = dedent(frmt).format(*args)
    return code_mem


def demo_def(a=None):
    """dummy...
    : Demonstrates retrieving and documenting module and function info.
    :
    """
    def sub(b):
       """sub in dummy"""
       return b**2
    #
    if a is None:
        a = 5
        b = sub(a)   
    return None


script = sys.argv[0]  # a useful way to get a file's name
"""
obj = None
if inspect.ismodule(obj):
    modu_mem = get_modu(obj)
elif inspect.iscode(obj):
    code_mem = get_func(obj)
elif inspect.ismethod(obj):
    meth_mem = [i[0] for i in inspect.getmembers(obj)]
    # **** work on this
#mem = [i[0] for i in inspect.getmembers(obj)]
"""

frmt = """
:----------------------------------------------------------------------
:Code for a function on line...{}...
{}
:Comments preceeding function
{}
:function?... {} ... or method? {}
:Module info...
{}
:
:Module functions...
{}    
:----------------------------------------------------------------------
"""
if __name__ == "__main__":
    """inspect module demo"""
    import __main__
    a = get_modu(__main__)  # art
    b = get_func(get_func)

