import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

size = 6

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

# print(permutations(size, size))

def permutations_dict(n, k):
    result = {}
    def dfs(path, index):
        if len(path) == k:
            result[''.join(path)] = {}
            return index + 1
        for i in range(1, n+1):
            if str(i) not in path:
                index = dfs(path + [str(i)], index)
        return index
    dfs([], 0)
    return result

nodes = permutations_dict(size, size)
# print(nodes)

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

# print(flip('1234', 1))
# print(flip('1234', 2))
# print(flip('1234', 3))
# print(flip('1234', 4))

def calculate_edges(nodes: dict, size: int):
    for node in nodes:
        for i in range(1, size+1):
            actual = flip(node, i)
            nodes[node][i] = actual
    return nodes

nodes = calculate_edges(nodes, size)
# print(nodes)


def create_graph(nodes: dict):
    G = nx.Graph()
    for node in nodes:
        for weight in nodes[node]:
            G.add_edge(node, nodes[node][weight], weight=weight)
    return G

graph = create_graph(nodes)

def show_graph(nodes: dict):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    # show the weights
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()

# show_graph(nodes)

def create_adjacency_list(nodes: dict):
    adjacency_list = {}
    for node in nodes:
        adjacency_list[node] = []
        for weight in nodes[node]:
            adjacency_list[node].append(nodes[node][weight])
    return adjacency_list

adjacency_list = create_adjacency_list(nodes)
# print(adjacency_list)

file = open("adjacency_list.txt", "w")
def show_adjacency_matrix(nodes: dict):
    matrix = ""
    firstRow = "\t".join(nodes.keys())
    matrix += "\t" + firstRow + "\n"
    for node in nodes.keys():
        matrix += node + "\t"
        for node2 in nodes.keys():
            if node2 in adjacency_list[node]:
                matrix += str(adjacency_list[node].count(node2)) + "\t"
            else:
                matrix += "0\t"
        matrix += "\n"
    file.write(matrix)
    print(matrix)


show_adjacency_matrix(nodes)
