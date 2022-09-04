from sympy import *
x = Symbol('x')
# Assumption about x
fact = [Q.prime(x)]
with assuming(*fact):
	print(ask(Q.rational(1 / x)))