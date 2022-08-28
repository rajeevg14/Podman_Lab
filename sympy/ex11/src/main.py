from sympy import *
x = Symbol('x')
y = Symbol('y')
facts = Q.positive(x), Q.positive(y)
with assuming(*facts):
	print(ask(Q.positive(2 * x + y)))