from sympy import pprint, init_printing, Symbol, sin, cos, exp, sqrt, series, Integral, Function
>>>
>>> x = Symbol("x")
>>> y = Symbol("y")
>>> f = Function('f')
>>> # pprint will default to unicode if available
>>> pprint( x**exp(x) )
 ⎛ x⎞
 ⎝ℯ ⎠
x   
>>> # An output without unicode
>>> pprint(Integral(f(x), x), use_unicode=False)
  /       
 |        
 | f(x) dx
 |        
/        
>>> # Compare with same expression but this time unicode is enabled
>>> pprint(Integral(f(x), x), use_unicode=True)
⌠        
⎮ f(x) dx
⌡     
>>> # Alternatively, you can call init_printing() once and pretty-print without the pprint function.
>>> init_printing()
>>> sqrt(sqrt(exp(x)))
   ____
4 ╱  x 
╲╱  ℯ  
>>> (1/cos(x)).series(x, 0, 10)