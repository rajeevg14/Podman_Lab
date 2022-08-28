from sympy import init_printing, Symbol, expand
init_printing()
a = Symbol('a')
b = Symbol('b')
e = (a + b)**3
print(e)
e.expand()