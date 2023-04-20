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
nPancakes = 4
start = '2431'
end = ''.join([str(i) for i in range(1, nPancakes+1)])

Model.start = start
Model.end = end

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
path = {}

def calculate_edges(nodes: list, size: int, edges: dict):
    for node in nodes:
        for i in range(1, size+1):
            actual = flip(node, i)
            edges[(node, actual)] = 1
            path[(node, actual)] = i
    return edges

calculate_edges(nodes, nPancakes, edges)
# print(len(edges))

Model.i = Set(initialize=nodes)
Model.j = Set(initialize=nodes)

Model.edges = Param(Model.i, Model.j, initialize=edges, default=999)

# VARIABLES****************************************************************************
Model.x = Var(Model.i, Model.j, domain=Binary)

# OBJECTIVE FUNCTION*******************************************************************
Model.obj = Objective(expr=sum(Model.x[i, j]*Model.edges[i, j] for i in Model.i for j in Model.j), sense=minimize)

# CONSTRAINTS**************************************************************************
def source_rule(Model,i):
    if i==Model.start:
        return sum(Model.x[i,j] for j in Model.j)==1
    else:
        return Constraint.Skip
Model.source = Constraint(Model.i, rule=source_rule)

def destination_rule(Model,j):
    if j==Model.end:
        return sum(Model.x[i,j] for i in Model.i)==1
    else:
        return Constraint.Skip
Model.destination = Constraint(Model.j, rule=destination_rule)

def intermediate_rule(Model,i):
    if i!=start and i!=end:
        return sum(Model.x[i,j] for j in Model.j) - sum(Model.x[j,i] for j in Model.i)==0
    else:
        return Constraint.Skip
Model.intermediate = Constraint(Model.i, rule=intermediate_rule)

def non_repeated_node_rule(Model,i,j):
    if i==j:
        return Model.x[i,j]==0
    else:
        return Constraint.Skip
Model.non_repeated_node = Constraint(Model.i, Model.j, rule=non_repeated_node_rule)

def non_repeated_edge_rule(Model,i,j):
    if i!=j:
        return Model.x[i,j]+Model.x[j,i]<=1
    else:
        return Constraint.Skip
Model.non_repeated_edge = Constraint(Model.i, Model.j, rule=non_repeated_edge_rule)

# APPLYING THE SOLVER******************************************************************
SolverFactory('glpk').solve(Model)

Model.obj.display()

G = nx.DiGraph()
G.add_nodes_from(nodes)
for edge in Model.edges:
    if Model.edges[edge] == 1:
        G.add_edge(edge[0], edge[1])

G2 = nx.DiGraph() # G2 es el grafo con las aristas que se usaron para llegar a la solución
G2.add_nodes_from(nodes)
for edge in Model.edges:
    if Model.edges[edge] == 1 and Model.x[edge].value != 0.0:
        G2.add_edge(edge[0], edge[1])

print("cambios de de estado: ", " ".join(str(i) for i in G2.edges))

resultPath = G2.edges
nFlips =  {i: 0 for i in range(1, nPancakes+1)}

for edge in resultPath:
    nFlips[path[edge]] += 1

print("Número de flips total: ", sum(nFlips.values()))
print("Número de flips por cada tamaño de pila: ")
for i in range(1, nPancakes+1):
    print(" - ", i, ": ", nFlips[i])

pos = nx.spring_layout(G)
pos = nx.circular_layout(G)
pos = nx.kamada_kawai_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=3, alpha=0.2, edge_color='black', connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# plot the edge labels the weights found in the path dictionary
edge_labels = {(i, j): path[(i, j)] for i, j in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')

nx.draw_networkx_nodes(G2, pos, node_size=700)
nx.draw_networkx_edges(G2, pos, width=3, alpha=1, edge_color='red', connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_labels(G2, pos, font_size=10, font_family='sans-serif')

plt.axis('off')
plt.show()
