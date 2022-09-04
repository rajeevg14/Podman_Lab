from sympy import Symbol, cos, sin, pprint
x = Symbol('x')
e = 1/cos(x)
pprint(e)
pprint(e.series(x, 0, 10))
e = 1/sin(x)
pprint(e)
pprint(e.series(x, 0, 4))