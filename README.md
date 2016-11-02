# Python
Python scripts and tools for ArcMap

inspect_demo.py   A script to document modules and/or functions

Output by inspecting one of the enclosed functions, returned as 'b'.
The 'Line number' is where it begins in the inspect_demo script/module.
The 'variable names' are just that...
The source code is provided with line numbers.

>>> print(b)

:-----------------------------------------------------------------
:Function: .... get_func ....
:Line number... 66
:Docs:
 
:Defaults: (True,)
:Keyword Defaults: None
:Variable names: ('obj', 'verbose', 'frmt', 'inspect', 'lines', 'ln_num', 'code', 'args', 'code_mem')
:Source code:
   0  def get_func(obj, verbose=True):
   1      """ """
   2      frmt = """
   3      :-----------------------------------------------------------------
   4      :Function: .... {} ....
   5      :Line number... {}
   6      :Docs:
   7      {}
   8      :Defaults: {}
   9      :Keyword Defaults: {}
  10      :Variable names: {}
  11      :Source code:
  12      {}
  13      :
  14      :-----------------------------------------------------------------
  15      """
  16      import inspect
  17      lines, ln_num = inspect.getsourcelines(obj)
  18      code = "".join(["{:4d}  {}".format(idx, line)
  19                      for idx, line in enumerate(lines)])
  20      #vars = 
  21      args = [obj.__name__, ln_num, obj.__doc__, obj.__defaults__,
  22              obj.__kwdefaults__, obj.__code__.co_varnames, code]        
  23      code_mem = dedent(frmt).format(*args)
  24      return code_mem

:
:-----------------------------------------------------------------



