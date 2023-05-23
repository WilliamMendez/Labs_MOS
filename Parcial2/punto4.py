import numpy as np
import matplotlib.pyplot as plt

def calcular_interseccion(A1, b1, A2, b2):
    # Calcular la intersección de dos restricciones
    A = np.vstack((A1, A2))
    b = np.hstack((b1, b2))
    intersection_point = np.linalg.solve(A, b)
    return intersection_point

def calcular_vertices():

    # Constraint 1: 2x1 + x2 <= 100
    A1 = np.array([[2, 1]])
    b1 = np.array([100])

    # Constraint 2: x1 + x2 <= 80
    A2 = np.array([[1, 1]])
    b2 = np.array([80])

    # Constraint 3: x1 <= 40
    A3 = np.array([[1, 0]])
    b3 = np.array([40])

    # Constraint 4: x2 >= 0
    A4 = np.array([[0, -1]])
    b4 = np.array([0])

    # Cañcular los vértices
    vertices = np.array([[0, 0], [0, b2[0]], [40, 0]])

    # Calcular los puntos de intersección
    intersection_points = []

    intersection_points.append(calcular_interseccion(A1, b1, A2, b2))
    intersection_points.append(calcular_interseccion(A1, b1, A3, b3))
    intersection_points.append(calcular_interseccion(A1, b1, A4, b4))
    intersection_points.append(calcular_interseccion(A2, b2, A3, b3))
    intersection_points.append(calcular_interseccion(A2, b2, A4, b4))

    intersection_points = np.array(intersection_points)

    feasible_intersection_points = []

    # Revisamos la viabilidad de los puntos de intersección y los agregamos a la lista realizando la multiplicación de matrices, si el resultado es menor o igual a b
    for point in intersection_points:
        if (np.dot(A1, point) <= b1 and np.dot(A2, point) <= b2
                and np.dot(A3, point) <= b3 and np.dot(A4, point) <= b4):
            feasible_intersection_points.append(point)
    feasible_intersection_points = np.array(feasible_intersection_points)

    return vertices, feasible_intersection_points

# Call the function to calculate the vertices and feasible intersection points
vertices, feasible_intersection_points = calcular_vertices()

print("Vertices:")
print(vertices)
print("Puntos de interseccion:")
print(feasible_intersection_points)

def plot_restricciones_verticeS_puntos(vertices, puntos):
    # Ploteamos las restricciones como rectas
    x = np.linspace(-10, 100, 1000)

    # Constraint 1: 2x1 + x2 <= 100
    y1 = 100 - 2 * x

    # Constraint 2: x1 + x2 <= 80
    y2 = 80 - x

    # Ploteamos las restricciones
    plt.plot(x, y1, label=r'$2x_1 + x_2 \leq 100$')
    plt.plot(x, y2, label=r'$x_1 + x_2 \leq 80$')
    
    # Plotear las restricciones verticales y horizontales con linea punteada
    plt.plot([40, 40], [-10, 100], label= r'$x_1 \leq 40$', linestyle='--')
    plt.plot([-10, 100], [0, 0], label= r'$x_2 \geq 0$', linestyle='--')
    plt.plot([0, 0], [-10, 100], label= r'$x_1 \geq 0$', linestyle='--')

    # Ploteamos los vértices y ponemos su coordenada al lado
    plt.plot(vertices[:, 0], vertices[:, 1], 'bo', label='Vertices')
    for i, vertex in enumerate(vertices):
        plt.text(vertex[0], vertex[1], f'({vertex[0]}, {vertex[1]})', fontsize=10)

    # Ploteamos los puntos de intersección y ponemos su coordenada al lado
    plt.plot(puntos[:, 0], puntos[:, 1], 'ro', label='Puntos de interseccion')
    for i, point in enumerate(puntos):
        plt.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=10)

    plt.xlim(-10, 100)
    plt.ylim(-10, 100)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.legend()
    plt.grid()
    plt.show()

# En caso de querer hacer un plot del problema y ver la region con sus restricciones, descomentar la siguiente linea
plot_restricciones_verticeS_puntos(vertices, feasible_intersection_points)

# Unimos los vertices con los puntos de interseccion
vertices = np.vstack((vertices, feasible_intersection_points))
print(vertices)

# Buscamos los vectores adyacentes a cada vertice y los guardamos en un diccionario donde la llave es el vertice y el valor es una lista de los vectores adyacentes
adyacentes = {}

# Asignamos los vectores adyacentes a cada vertice manualmente
adyacentes[tuple(vertices[0])] = [tuple(vertices[1]), tuple(vertices[2])]
adyacentes[tuple(vertices[1])] = [tuple(vertices[0]), tuple(vertices[3])]
adyacentes[tuple(vertices[2])] = [tuple(vertices[0]), tuple(vertices[4])]
adyacentes[tuple(vertices[3])] = [tuple(vertices[1]), tuple(vertices[4])]
adyacentes[tuple(vertices[4])] = [tuple(vertices[2]), tuple(vertices[3])]

def simplex_woodcarve(vertices, adyacentes):
    
    # Ahora calculamos el valor de la funcion objetivo para cada vertice
    valores = {}
    for vertex in vertices:
        valores[tuple(vertex)] = 3*vertex[0] + 2*vertex[1]

    # Ahora empezamos el algortimo desde un vertice aleatorio
    FEV = tuple(vertices[np.random.randint(0, len(vertices))])
    print(f"Vertice inicial: {FEV}")
    print(f"Valor funcion Obj: {valores[FEV]}")
    print(f"Adyacentes: {adyacentes[FEV]}")
    print()

    maxVal = 0
    maxVertex = None
    # Ahora empezamos el algoritmo
    while True:
        # Buscamos el vertice adyacente con el mayor valor de la funcion objetivo

        for vertex in adyacentes[FEV]:
            if valores[vertex] > maxVal:
                maxVal = valores[vertex]
                maxVertex = vertex
            
        # Si el vertice actual es el optimo, terminamos el algoritmo
        if maxVertex == FEV:
            break

        # Si no, actualizamos el vertice actual y el FEV
        FEV = maxVertex

    print("------------------------- Resultado -------------------------")
    print(f"Vertice final: {FEV}")
    print(f"Valor funcion Obj: {valores[FEV]}")
    print()

    return FEV

vertice_optimo = simplex_woodcarve(vertices, adyacentes)


