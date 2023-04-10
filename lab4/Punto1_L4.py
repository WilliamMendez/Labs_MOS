"""
*************************************************************************
***      Ejercicio 1 Laboratorio 4                                    ***
*************************************************************************
"""

from pyomo.environ import *

Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
Model.i = {'o1', 'o2', 'o3'}
Model.j = {'d1', 'd2'}

Model.ofertaKernel = Param(Model.i, initialize={'o1': 60, 'o2': 80, 'o3': 50})

Model.ofertaUsuario = Param(Model.i, initialize={'o1': 80, 'o2': 50, 'o3': 50})

Model.demandaUsuario = Param(Model.j, initialize={'d1': 60, 'd2': 120})

Model.demandaKernel = Param(Model.j, initialize={'d1': 100, 'd2': 90})

Model.costo = Param(Model.i, Model.j, initialize={('o1', 'd1'): 300, ('o1', 'd2'): 500,('o2', 'd1'): 200, ('o2', 'd2'): 300,('o3', 'd1'): 600, ('o3', 'd2'): 300})

# VARIABLES****************************************************************************
Model.x = Var(Model.i, Model.j, domain=NonNegativeIntegers)
Model.y = Var(Model.i, Model.j, domain=NonNegativeIntegers)

# OBJECTIVE FUNCTION*******************************************************************
Model.obj = Objective(expr=sum(Model.costo[i, j] * (Model.x[i, j] + Model.y[i, j]) for i in Model.i for j in Model.j), sense=minimize)

# CONSTRAINTS**************************************************************************
def ofertaKernel_rule(Model, i):
    return sum(Model.x[i, j] for j in Model.j) == Model.ofertaKernel[i]
Model.ofertaKernel_con = Constraint(Model.i, rule=ofertaKernel_rule)

def demandaKernel_rule(Model, j):
    return sum(Model.x[i, j] for i in Model.i) == Model.demandaKernel[j]
Model.demandaKernel_con = Constraint(Model.j, rule=demandaKernel_rule)

def ofertaUsuario_rule(Model, i):
    return sum(Model.y[i, j] for j in Model.j) == Model.ofertaUsuario[i]
Model.ofertaUsuario_con = Constraint(Model.i, rule=ofertaUsuario_rule)

def demandaUsuario_rule(Model, j):
    return sum(Model.y[i, j] for i in Model.i) == Model.demandaUsuario[j]
Model.demandaUsuario_con = Constraint(Model.j, rule=demandaUsuario_rule)

# APPLYING THE SOLVER******************************************************************
SolverFactory('glpk').solve(Model)

Model.display()