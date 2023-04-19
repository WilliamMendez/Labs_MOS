#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

import sys
import os

import itertools

os.system("cls")

#sys.exit("Stopped")

Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
numNodes=4
N=range(numNodes) #[0, 1, 2, 3]

S=[]
for L in range(0, len(N)+1):
    for subset in itertools.combinations(N, L):
        if len(subset)>=2:
            S.append(subset)

#cost={(0,0):999, (0,1):1, (0,2):2,   (0,3):999,\
#      (1,0):1, (1,1):999, (1,2):3, (1,3):1,\
#      (2,0):2, (2,1):3, (2,2):999, (2,3):2,  \
#      (3,0):1, (3,1):1, (3,2):2, (3,3):999}

cost={}
for i in N:
    for j in N:
        cost[i,j]=999

cost[1,0]=1
cost[2,0]=2
cost[3,0]=1

cost[0,1]=1
cost[2,1]=3
cost[3,1]=1

cost[0,2]=2
cost[1,2]=3
cost[3,2]=2

cost[1,3]=1
cost[2,3]=2 
    
# VARIABLES****************************************************************************
Model.x = Var(N,N, domain=Binary)

# OBJECTIVE FUNCTION*******************************************************************
Model.obj = Objective(expr = sum(Model.x[i,j]*cost[i,j] for i in N for j in N))

Model.res1 = Constraint(expr = sum(Model.x[i,j] for i in N for j in N)==len(N)-1)

Model.rests=ConstraintList()
k=-1
for element in S:
    k=k+1
    Model.rests.add(
            sum(Model.x[i,j] for i in S[k] for j in S[k])<=len(S[k])-1)

def notRepLinkRule(Model,i,j):
    return Model.x[i,j] + Model.x[j,i]<=1
    
Model.notRepLink=Constraint(N,N, rule=notRepLinkRule)

# APPLYING THE SOLVER******************************************************************
#SolverFactory('glpk').solve(Model)

solver=SolverFactory('glpk')
#solver.options['ItLim'] = 100
solver.solve(Model,tee=True)

Model.display()



