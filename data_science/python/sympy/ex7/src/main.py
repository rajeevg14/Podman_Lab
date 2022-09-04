from sympy import init_printing, Symbol, limit, sqrt, oo
init_printing()
x = Symbol('x')
limit(sqrt(x**2 - 5*x + 6) - x, x, oo)
limit(x*(sqrt(x**2 + 1) - x), x, oo)
limit(1/x**2, x, 0)
z = limit(((x - 1)/(x + 1))**x, x, oo)

print(z)