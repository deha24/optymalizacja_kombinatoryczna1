#example of usage: python GreedyRandomized.py 10000 27 15 500000
#generates 10000 random connected graphs with 15 nodes and 27 edges
#then optimizes the best one using hill climbing (500000 iterations)
# finally displaying in graph6 format

import random
import sys
import numpy as np

def convert_to_graph6(matrix):

    bits = []

    for i in range(1, len(matrix)):
        for j in range(i):
            bits.append(str(matrix[i][j]))

    bits_join= "".join(bits)

    while (len(bits_join))%6 !=0:
        bits_join += "0"

    graph6 = chr(len(matrix)+63)

    for i in range(0, len(bits_join),6):
        package = bits_join[i : i+6]
        value = int(package,2)
        graph6 += chr(value+63)

    return graph6

def convert_to_adjacency_list(matrix):
    adj = []

    n = len(matrix)

    for i in range(n):
        row = []
        for j in range(n):
            if matrix[i][j] == 1:
                row.append(j)
        adj.append(row)
    return adj

def generateGraph(n,k):

    max_k = n*(n-1)//2

    k_arr = np.zeros(max_k, dtype=int)
    k_arr[:k] = 1
    np.random.shuffle(k_arr)

    matrix = np.zeros((n, n), dtype=int)
    lower_triangle = np.tril_indices(n, -1)

    matrix[lower_triangle] = k_arr

    matrix = matrix + matrix.T

    while dfs(convert_to_adjacency_list(matrix)) == False:
        matrix = generateGraph(n,k)

    return matrix
            
def dfsRec(adjacency_list, visited, n, result):

    visited[n] = True
    result.append(n)

    for i in adjacency_list[n]:
        if not visited[i]:
            dfsRec(adjacency_list, visited, i, result)

def dfs(adjacency_list):
    visited = [False] * len(adjacency_list)
    result = []
    dfsRec(adjacency_list, visited, 0, result)
    if all(visited):
        return result
    return False

def calculate_einvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

def calculate_score(eigenvalues):
    energy = sum(abs(ev - np.round(ev)) for ev in eigenvalues)
    return energy

def mutate_graph(matrix):
    n = len(matrix)

    existing_edges = [(i, j) for i in range(n) for j in range(i) if matrix[i][j] == 1]
    empty_slots = [(i, j) for i in range(n) for j in range(i) if matrix[i][j] == 0]

    if not existing_edges or not empty_slots:
        return None
    
    edge_to_remove = random.choice(existing_edges)
    edge_to_add = random.choice(empty_slots)

    new_matrix = [row[:] for row in matrix]

    u, v = edge_to_remove
    new_matrix[u][v] = 0
    new_matrix[v][u] = 0

    x, y = edge_to_add
    new_matrix[x][y] = 1
    new_matrix[y][x] = 1

    if dfs(convert_to_adjacency_list(new_matrix)) == False:
        return None

    return new_matrix

def hill_climbing(initial_matrix, max_iterations):
    current_matrix = initial_matrix
    current_score = calculate_score(calculate_einvalues(current_matrix))

    for _ in range(max_iterations):
        new_matrix = mutate_graph(current_matrix)

        if new_matrix is None:
            continue

        new_matrix_score = calculate_score(calculate_einvalues(new_matrix))

        if new_matrix_score < current_score:
            current_matrix = new_matrix
            current_score = new_matrix_score
        if current_score < 1e-9:
            return current_matrix, current_score

    return current_matrix, current_score
 
if __name__ == "__main__":
    rep = int(sys.argv[1]) if (len(sys.argv)>1) else 10000
    k = int(sys.argv[2]) if (len(sys.argv)>2) else 27
    n = int(sys.argv[3]) if (len(sys.argv)>3) else 15
    iterations = int(sys.argv[4]) if (len(sys.argv)>4) else 500000
    best_matrix = None
    best_matrix_score = 10

    for i in range(rep):
        matrix = generateGraph(n,k)
        if calculate_score(calculate_einvalues(matrix)) < best_matrix_score:
            best_matrix = matrix
            best_matrix_score = calculate_score(calculate_einvalues(matrix))

    best_matrix, best_matrix_score = hill_climbing(best_matrix, iterations)
    print(convert_to_graph6(best_matrix))