import pycuda
import pycuda.autoinit
from pycuda.tools import make_default_context
c = make_default_context()
d = c.get_device()
print(d.name())