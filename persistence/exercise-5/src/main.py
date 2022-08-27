import pyomo.environ as pyo
from itertools import compress

pyomo_solvers_list = pyo.SolverFactory.__dict__['_cls'].keys()
solvers_filter = []
for s in pyomo_solvers_list:
    try:
        solvers_filter.append(pyo.SolverFactory(s).available())
    except (ApplicationError, NameError, ImportError) as e:
        solvers_filter.append(False)
pyomo_solvers_list = list(compress(pyomo_solvers_list,solvers_filter))
print(pyomo_solvers_list)