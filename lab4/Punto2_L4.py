"""
*************************************************************************
***      Ejercicio 2 Laboratorio 3                                    ***
*************************************************************************
"""

from pyomo.environ import *

Model = ConcreteModel()

# Sets
Model.i = {"p1", "p2", "p3", "p4", "p5", "p6"}
Model.j = {"p1", "p2", "p3", "p4", "p5", "p6"}

# Variables
Model.x = Var(Model.i, domain=Binary)

tp_original = {
    ("p1", "p1"): 0,
    ("p1", "p2"): 10,
    ("p1", "p3"): 20,
    ("p1", "p4"): 30,
    ("p1", "p5"): 30,
    ("p1", "p6"): 20,
    ("p2", "p1"): 10,
    ("p2", "p2"): 0,
    ("p2", "p3"): 25,
    ("p2", "p4"): 35,
    ("p2", "p5"): 20,
    ("p2", "p6"): 10,
    ("p3", "p1"): 20,
    ("p3", "p2"): 25,
    ("p3", "p3"): 0,
    ("p3", "p4"): 15,
    ("p3", "p5"): 30,
    ("p3", "p6"): 20,
    ("p4", "p1"): 30,
    ("p4", "p2"): 35,
    ("p4", "p3"): 15,
    ("p4", "p4"): 0,
    ("p4", "p5"): 15,
    ("p4", "p6"): 25,
    ("p5", "p1"): 30,
    ("p5", "p2"): 20,
    ("p5", "p3"): 30,
    ("p5", "p4"): 15,
    ("p5", "p5"): 0,
    ("p5", "p6"): 14,
    ("p6", "p1"): 20,
    ("p6", "p2"): 10,
    ("p6", "p3"): 20,
    ("p6", "p4"): 25,
    ("p6", "p5"): 14,
    ("p6", "p6"): 0
}

for i in Model.i:
    for j in Model.j:
        if tp_original[i, j] <= 15:
            tp_original[i, j] = 1
        if tp_original[i, j] > 15:
            tp_original[i, j] = 0

Model.tp = Param(Model.i, Model.j, initialize=tp_original)

# Equations
Model.obj = Objective(expr=sum(Model.x[i] for i in Model.i), sense=minimize)

def restriccionTiempo_rule(Model, i):
    return sum(Model.x[j] * Model.tp[i, j] for j in Model.j) == 1
Model.restriccionTiempo = Constraint(Model.i, rule=restriccionTiempo_rule)

# Solve
opt = SolverFactory("glpk")
results = opt.solve(Model)

# Display results
Model.display()
Model.x.display()
