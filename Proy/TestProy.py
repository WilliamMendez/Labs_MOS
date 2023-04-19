from pyomo.environ import *
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt
import networkx as nx

"""
*************************************************************************
***      Proyecto                                                     ***
*************************************************************************
"""


Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
nPancakes = 3
start = '132'
end = '123'

def permutations(n, k):
    result = []
    def dfs(path):
        if len(path) == k:
            result.append(''.join(path))
            return
        for i in range(1, n+1):
            if str(i) not in path:
                dfs(path + [str(i)])
    dfs([])
    return result

nodes = permutations(nPancakes, nPancakes)

def flip(s, k):
    if k == 1:
        return s
    else:
        first = s[:k]
        # print(first)
        first = first[::-1]
        # print(first)
        second = s[k:]
        # print(second)
        return first + second

edges = {(i, j): 999 for i in nodes for j in nodes}

def calculate_edges(nodes: list, size: int, edges: dict):
    for node in nodes:
        for i in range(1, size+1):
            actual = flip(node, i)
            edges[(node, actual)] = 1
    return edges

calculate_edges(nodes, nPancakes, edges)
print(len(edges))

Model.i = Set(initialize=nodes)
Model.j = Set(initialize=nodes)

Model.adj = Param(Model.i, Model.j, initialize=edges, default=999)

# VARIABLES****************************************************************************
Model.x = Var(Model.i, Model.j, domain=Binary)

# OBJECTIVE FUNCTION*******************************************************************
Model.obj = Objective(expr=sum(Model.x[i, j]*Model.adj[i, j] for i in Model.i for j in Model.j), sense=minimize)

# CONSTRAINTS**************************************************************************
def source_rule(Model,i):
    if i==start:
        return sum(Model.x[i,j] for j in Model.j)==1
    else:
        return Constraint.Skip
Model.source = Constraint(Model.i, rule=source_rule)

def destination_rule(Model,j):
    if j==end:
        return sum(Model.x[i,j] for i in Model.i)==1
    else:
        return Constraint.Skip
Model.destination = Constraint(Model.j, rule=destination_rule)

def intermediate_rule(Model,i,j):
    if i!=start and j!=end:
        return sum(Model.x[i,k] for k in Model.j)-sum(Model.x[k,j] for k in Model.i)==0
    else:
        return Constraint.Skip
Model.intermediate = Constraint(Model.i, Model.j, rule=intermediate_rule)

def non_repeated_rule(Model,i,j):
    return Model.x[i,j]+Model.x[j,i]<=1
Model.non_repeated = Constraint(Model.i, Model.j, rule=non_repeated_rule)

# APPLYING THE SOLVER******************************************************************
SolverFactory('glpk').solve(Model)

Model.display()
Model.adj.display()
Model.x.display()

G = nx.DiGraph()
G.add_nodes_from(nodes)
for edge in edges:
    if edges[edge] == 1:
        G.add_edge(edge[0], edge[1])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color='black')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

G = nx.DiGraph()
G.add_nodes_from(nodes)
for edge in edges:
    if edges[edge] == 1 and Model.x[edge[0], edge[1]].value == 1:
        G.add_edge(edge[0], edge[1])

nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color='red')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
