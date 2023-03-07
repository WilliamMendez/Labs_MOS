import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# string de la tabla separado por espacios
tabla = '0 1 1 0 1 0 0 0 0 0 0 0 \
          1 0 0 0 1 0 0 0 0 0 0 0 \
          1 0 0 1 1 1 1 1 0 0 0 0 \
          0 0 1 0 1 1 0 0 0 0 1 0 \
          1 1 1 1 0 0 0 0 0 1 1 0 \
          0 0 1 1 0 0 0 1 0 0 1 0 \
          0 0 1 0 0 0 0 1 0 0 0 1 \
          0 0 1 0 0 1 1 0 1 0 1 1 \
          0 0 0 0 0 0 0 1 0 1 1 1 \
          0 0 0 0 1 0 0 0 1 0 1 0 \
          0 0 0 1 1 1 0 1 1 1 0 0 \
          0 0 0 0 0 0 1 1 1 0 0 0'

# convertir el string en una matriz de adyacencias
matriz = np.array([int(i) for i in tabla.split()]).reshape((12, 12))

# crear el grafo utilizando NetworkX
G = nx.from_numpy_matrix(matriz)

# generar posiciones de los nodos
pos = nx.spring_layout(G)

# dibujar el grafo
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
