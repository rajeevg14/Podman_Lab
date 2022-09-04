from sympy import init_printing, symbols, ln, diff
init_printing()
x, y = symbols('x y')
f = x**2 / y + 2 * x - ln(y)
diff(f, x)
diff(f, y)
z = diff(diff(f, x), y)
print(z)