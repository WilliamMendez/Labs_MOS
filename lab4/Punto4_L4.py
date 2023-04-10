"""
*************************************************************************
***      Ejercicio 4 Laboratorio 2                                    ***
*************************************************************************
"""

from pyomo.environ import *
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt

Model = ConcreteModel()

# Sets
Model.nodos = Set(initialize=['1','2','3','4','5','6','7'])
Model.i = Set(initialize=['1','2','3','4','5','6','7'])
Model.j = Set(initialize=['1','2','3','4','5','6','7'])

# Parameters

x = {'1':20,'2':22,'3':9,'4':3,'5':21,'6':29,'7':14}
y = {'1':6,'2':1,'3':2,'4':25,'5':10,'6':2,'7':12}
dist = {}

for i in Model.i:
    for j in Model.j:
        if i == j:
            dist[i,j] = 1000000
        else:
            dist_x_y = sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if dist_x_y > 20:
                dist[i,j] = 1000000
            else:
                dist[i,j] = dist_x_y

Model.d = Param(Model.i,Model.j,initialize=dist)


# Variables
Model.si_no = Var(Model.i,Model.j,within=Binary)


# Equations
Model.obj = Objective(expr=sum(Model.d[i,j]*Model.si_no[i,j] for i in Model.i for j in Model.j),sense=minimize)

def source_node_rule(Model,i):
    if i == '4':
        return sum(Model.si_no[i,j] for j in Model.j) == 1
    else:
        return Constraint.Skip

Model.source_node = Constraint(Model.i,rule=source_node_rule)

def destination_node_rule(Model,j):
    if j == '6':
        return sum(Model.si_no[i,j] for i in Model.i) == 1
    else:
        return Constraint.Skip

Model.destination_node = Constraint(Model.j,rule=destination_node_rule)

def intermediate_node_rule(Model,i):
    if i != '4' and i != '6':
        return sum(Model.si_no[i,j] for j in Model.j) - sum(Model.si_no[j,i] for j in Model.j) == 0
    else:
        return Constraint.Skip

Model.intermediate_node = Constraint(Model.i,rule=intermediate_node_rule)


# Solve
SolverFactory('glpk').solve(Model)
Model.display()
# Model.d.display()

# Print the results
plt.figure()
plt.style.use('ggplot')

for i in Model.nodos:
    plt.scatter(x[i],y[i], c='black')
    plt.text(x[i]+0.3, y[i],i)

for i, j in Model.d:
    if Model.d[i,j] < 999:
        plt.plot([x[i],x[j]],[y[i],y[j]], ':', c='black')


for i, j in Model.si_no:
    if Model.si_no[i,j].value > 0:
        plt.plot([x[i],x[j]],[y[i],y[j]], c='red')

plt.show()
