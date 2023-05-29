from pyomo.environ import *
from pyomo.opt import SolverFactory

Model = ConcreteModel()

# I1 = 4
# I2 = 6
# I3 = 8
# I4 = 18
# Vn = In*Rn (n = 1,2,3,4)
# V1 = V2 = V3
# 2 <= Vi <= 10 (i = 1,2,3,4)
# Potencia disipada sum(In^2*Rn)    Objetivo: Minimizar

Model.i = Set(initialize=[1,2,3,4])

Model.In = Param(Model.i, initialize={1:4, 2:6, 3:8, 4:18})

Model.Vn = Var(Model.i, bounds=(2,10))
Model.Rn = Var(Model.i)

Model.obj = Objective(expr=sum(Model.In[i]**2*Model.Rn[i] for i in Model.i))

Model.c1 = Constraint(expr=Model.Vn[1] == Model.Vn[2])
Model.c2 = Constraint(expr=Model.Vn[2] == Model.Vn[3])

def c3_rule(Model, i):
    return Model.Vn[i] == Model.In[i]*Model.Rn[i]
Model.c3 = Constraint(Model.i, rule=c3_rule)

SolverFactory('glpk').solve(Model)

Model.display()
Model.Rn.display()
Model.Vn.display()

