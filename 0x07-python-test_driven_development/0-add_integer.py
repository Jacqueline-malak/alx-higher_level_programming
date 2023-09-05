
" " " 
a module that adds 2 integers
it return ana integer
" " "

def add_integer(a, b=98):
    """
    returns the addition of a and b 
    or error if a and b is not an integer or float """
    if type(a) is not int and type (a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type (b) is not float:
        raise TypeError("b must be an integer")
  """ 
  casting a and b to be an integer value
  """
  if type(a) is float:
      a = int(a)
      if type(b) is float:
          b  = int(b)
          return a + b 
