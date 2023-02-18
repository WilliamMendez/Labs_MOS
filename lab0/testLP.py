
from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

# M = model
M = ConcreteModel()

M.x = Var([1,2], domain=NonNegativeReals)

M.obj = Objective(expr = 3*M.x[1] + 2*M.x[2], sense=maximize)

M.res1 = Constraint(expr = 2*M.x[1] + M.x[2] <= 100)

M.res2 = Constraint(expr = M.x[1] + M.x[2] <= 80)

M.res3 = Constraint(expr = M.x[1] <= 40)

SolverFactory('glpk').solve(M)

M.display()


