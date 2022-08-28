from sympy import init_printing, Symbol, Function, Eq, dsolve, sin, diff
init_printing()
x = Symbol("x")
f = Function("f")
eq = Eq(f(x).diff(x), f(x))
eq              
dsolve(eq, f(x))
eq = Eq(x**2*f(x).diff(x), -3*x*f(x) + sin(x)/x)
eq
z = dsolve(eq, f(x))

print(z)