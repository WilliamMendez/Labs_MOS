import heapq
import math

coords = {'1': (20, 6),
          '2': (22, 1),
          '3': (9, 2),
          '4': (3, 25),
          '5': (21, 10),
          '6': (29, 2),
          '7': (14, 12)}

costos = [[0 for i in range(7)] for j in range(7)]

for i in range(1, 8):
    for j in range(1, 8):
        if i != j:
            costos[i-1][j-1] = math.sqrt((coords[str(i)][0] - coords[str(j)][0])**2 + (
                coords[str(i)][1] - coords[str(j)][1])**2)
            costos[i-1][j-1] = round(costos[i-1][j-1], 2)
            if costos[i-1][j-1] > 20:
                costos[i-1][j-1] = 'Z'
        else:
            costos[i-1][j-1] = 'Z'


def printTable(table):
    for i in range(7):
        for j in range(7):
            print(table[i][j], end=' ')
        print()


printTable(costos)

# convert to adjascent matrix
adj = {i: [] for i in range(1, 8)}
for i in range(7):
    for j in range(7):
        if costos[i][j] != 'Z':
            adj[i+1].append(j+1)

for i in adj:
    print(i, adj[i])

# mimimize cost from 4 to 6 using Dijkstra's algorithm


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    selectedPath = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        currentDistance, currentNode = heapq.heappop(queue)
        if currentDistance > distances[currentNode]:
            continue
        for adjacent, weight in graph[currentNode].items():
            distance = currentDistance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                selectedPath.append([currentNode, adjacent])
    print(selectedPath)

    return distances[end]


graph = {i: {} for i in range(1, 8)}
for i in range(7):
    for j in range(7):
        if costos[i][j] != 'Z':
            graph[i+1][j+1] = costos[i][j]

print(dijkstra(graph, 4, 6))
