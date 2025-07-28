# Reference Obsidian 32.04.02 - Python Classes and Self Syntax
#https://docs.python.org/3/tutorial/classes.html

class C:
  def foo(self):
    print("Hi!")

def bar(self):
  print("Bork bork bork!")

c = C()
C.bar = bar
c.bar()
# Bork bork bork!

c.foo()
#Hi!