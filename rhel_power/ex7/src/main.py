import numpy as np

#Rosenbrock Function
def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])
   
from scipy.optimize import least_squares

input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print (res)