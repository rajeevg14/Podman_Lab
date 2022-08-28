from sympy import init_printing, integrate, Symbol, exp, cos, erf
init_printing()
x = Symbol('x')
# Polynomial Function
f = x**2 + x + 1
f       
integrate(f,x)   
# Rational Function
f = x/(x**2+2*x+1)
f
integrate(f, x)
# Exponential-polynomial functions
f = x**2 * exp(x) * cos(x)
f
integrate(f, x)
# A non-elementary integral
f = exp(-x**2) * erf(x)
f
z= integrate(f, x)

print(z)