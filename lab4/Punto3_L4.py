"""
*************************************************************************
***      Ejercicio 4 Laboratorio 3                                    ***
*************************************************************************
  Las losas se nombraron con el alfabeto de manera que se representan
  de la siguiente manera:
         a b c d
         e f g h
         i j k l
         m n o p
         q r s t
"""
from pyomo.environ import *

Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
Model.i = {"1", "2", "3", "4", "5", "6", "7"} # tubos
Model.j = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"} # losas

cubre = {
    ("1", "a"): 1,
    ("1","e"): 1,
    ("2","e"): 1,
    ("2","i"): 1,
    ("3","b"): 1,
    ("3","c"): 1,
    ("3","f"): 1,
    ("3","g"): 1,
    ("4","i"): 1,
    ("4","j"): 1,
    ("4","m"): 1,
    ("4","n"): 1,
    ("5","j"): 1,
    ("5","k"): 1,
    ("5","n"): 1,
    ("5","o"): 1,
    ("6","m"): 1,
    ("6","q"): 1,
    ("7","s"): 1,
    ("7","t"): 1,
    ("7","p"): 1,
    ("7","l"): 1,
    ("7","h"): 1,
}

# Llenamos los que no estan en el diccionario con 0
for i in Model.i:
    for j in Model.j:
        if (i, j) not in cubre:
            cubre[i, j] = 0

Model.cubre = Param(Model.i, Model.j, initialize=cubre)

# VARIABLES****************************************************************************
Model.losas = Var(Model.j, domain=Binary)

# Equations
Model.obj = Objective(expr=sum(Model.losas[j] for j in Model.j), sense=minimize)

def unaPorZona_rule(Model, i):
    return sum(Model.losas[j] * Model.cubre[i, j] for j in Model.j) == 1
Model.restriccionTiempo = Constraint(Model.i, rule=unaPorZona_rule)

# Solve
opt = SolverFactory("glpk")
results = opt.solve(Model)

# Display results
Model.display()