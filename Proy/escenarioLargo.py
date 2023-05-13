from pyomo.environ import *
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt
import networkx as nx

from datetime import datetime

"""
*************************************************************************
***      Proyecto                                                     ***
*************************************************************************
"""

print("*************************************************************************")
print("Creando el modelo...")
Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
nPancakes = 6
print("Número de pancakes:", nPancakes)

start = '526431'
end = ''.join([str(i) for i in range(1, nPancakes+1)])

Model.start = start
Model.end = end

def permutations(n, k):
    time = datetime.now()
    result = []
    def dfs(path):
        if len(path) == k:
            result.append(''.join(path))
            return
        for i in range(1, n+1):
            if str(i) not in path:
                dfs(path + [str(i)])
    dfs([])
    print("Tiempo para las permutaciones:", datetime.now() - time)
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
    time = datetime.now()
    for node in nodes:
        for i in range(1, size+1):
            actual = flip(node, i)
            edges[(node, actual)] = 1
            path[(node, actual)] = i
    print("Tiempo para calcular los edges:", datetime.now() - time)
    return edges

calculate_edges(nodes, nPancakes, edges)
# print(len(edges))

time = datetime.now()
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

print("Tiempos para crear el modelo:", datetime.now() - time)

# APPLYING THE SOLVER******************************************************************
print("Resolviendo el modelo...")
time = datetime.now()
SolverFactory('glpk').solve(Model)
print("Tiempo para resolver el modelo:", datetime.now() - time)

# PRINTING THE SOLUTION***************************************************************
print("Solucion: ")
Model.obj.display()

time = datetime.now()
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

print("Tiempo para mostrar la solución:", datetime.now() - time)
time = datetime.now()

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, k=0.5, iterations=20)
# pos = nx.circular_layout(G, scale=4)
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

print("Tiempo para mostrar el grafo:", datetime.now() - time)

plt.axis('off')
plt.show()


# show the graph but only with the solution path
plt.figure(figsize=(10, 10))

g3 = nx.DiGraph()
for edge in resultPath:
    g3.add_edge(edge[0], edge[1])

pos = nx.spring_layout(g3, k=0.5, iterations=20)
# pos = nx.circular_layout(G, scale=4)
pos = nx.kamada_kawai_layout(g3)

nx.draw_networkx_nodes(g3, pos, node_size=700)
nx.draw_networkx_edges(g3, pos, width=3, alpha=0.2, edge_color='black', connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_labels(g3, pos, font_size=10, font_family='sans-serif')

# plot the edge labels the weights found in the path dictionary
edge_labels = {(i, j): path[(i, j)] for i, j in g3.edges()}
nx.draw_networkx_edge_labels(g3, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')

# nx.draw_networkx_nodes(G2, pos, node_size=700)
# nx.draw_networkx_edges(G2, pos, width=3, alpha=1, edge_color='red', connectionstyle='arc3, rad = 0.1')
# nx.draw_networkx_labels(G2, pos, font_size=10, font_family='sans-serif')

plt.axis('off')
plt.show()
