# -*- coding: utf-8 -*-

from pyomo.environ import *
from pyomo.opt import SolverFactory

Model = ConcreteModel()

A = [1,2,3,4]

xx = {1:2 , 2:6, 3:2, 4:6}
yy = {1:1, 2:1, 3:5, 4:5}
demanda = {1:100, 2:200, 3:300, 4:400}

#Model.x = Var(domain=PositiveReals, initialize = 2)
#Model.y = Var(domain=PositiveReals, initialize = 1)

Model.x = Var(domain=PositiveReals)
Model.y = Var(domain=PositiveReals)


Model.g = Objective(expr= sum((demanda[i]*((xx[i]-Model.x)**2+(yy[i]-Model.y)**2)**(1/2)) for i in A) , sense=minimize)

SolverFactory('ipopt').solve(Model)

Model.display()
