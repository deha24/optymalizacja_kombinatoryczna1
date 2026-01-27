#example of usage: python simulatedAnnealing.py 15 27 20.0 0.99998 500000
#generates a random connected graph with 15 nodes and 27 edges
#then optimizes it using simulated annealing wtih parameters:
#initial temperature 20.0, cooling rate 0.99998, max iterations 500000
#finally displaying in graph6 format

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

    while dfs(convert_to_adjacency_list(new_matrix)) == False:
        new_matrix = mutate_graph(matrix)

    return new_matrix

def calculate_einvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

def calculate_score(eigenvalues):
    score = sum(abs(ev - np.round(ev)) for ev in eigenvalues)
    return score

def simulated_annealing(initial_matrix, initial_temperature, cooling_rate, max_iterations):
    current_matrix = initial_matrix
    current_score = calculate_score(calculate_einvalues(current_matrix))
    best_matrix = current_matrix
    best_score = current_score
    temperature = initial_temperature

    for _ in range(max_iterations):
        if best_score < 1e-9:
            print(convert_to_graph6(best_matrix))
            break

        neighbor = mutate_graph(current_matrix)
        while neighbor is None:
            neighbor = mutate_graph(current_matrix)
        neighbor_score = calculate_score(calculate_einvalues(neighbor))
        score_diff = neighbor_score - current_score

        if score_diff < 0 or random.uniform(0, 1) < np.exp(-score_diff / temperature):
            current_matrix = neighbor
            current_score = neighbor_score

            if current_score < best_score:
                best_matrix = current_matrix
                best_score = current_score
        temperature *= cooling_rate

    return best_matrix, best_score

if __name__ == "__main__":
    n = int(sys.argv[1]) if (len(sys.argv)>1) else 15
    k = int(sys.argv[2]) if (len(sys.argv)>2) else 27
    initial_temperature = int(sys.argv[3]) if (len(sys.argv)>3) else 20.0
    cooling_rate = float(sys.argv[4]) if (len(sys.argv)>4) else 0.99998
    max_iterations = int(sys.argv[5]) if (len(sys.argv)>5) else 500000
    best_matrix = None
    best_matrix_score = 0

    matrix = generateGraph(n,k)

    optimized_matrix, optimized_score = simulated_annealing(matrix, initial_temperature, cooling_rate, max_iterations)

    print(convert_to_graph6(optimized_matrix))