# Reference Obsidian 32.04.01 - Python Defining Functions
#https://docs.python.org/3/tutorial/controlflow.html#defining-functions

def fib(n): # write Fibonacci series less than n
    """ Print a Fibonacci series less than n. (this is a string literal / function's documentation string / docstring) """
    a, b = 0, 1
    while a < n:
      print(a, end= ' ')
      a, b = b, a+b
    print()

fib(2000)