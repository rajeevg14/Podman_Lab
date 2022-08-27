import numpy as np
from scipy.optimize import rosen
a = 1.2 * np.arange(5)
b = rosen(a)
print(b)