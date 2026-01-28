#example of usage: python greedysub9.py 15 78
#it use a 9 nodes complete graph and mutate it node by node to kepp the closest spectral radius to n-1. 
#finally displaying in graph6 format

import sys
import numpy as np
import itertools

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

def convert_to_adjacency_matrix(graph6):

    n = ord(graph6[0]) - 63

    bits = []
    for char in graph6[1:]:
        val = ord(char) - 63
        for i in range(5, -1, -1):
            bits.append((val >> i) & 1)

    matrix = [[0] * n for _ in range(n)]
    cursor = 0

    for i in range(1, n):
        for j in range(i):
            if cursor < len(bits):
                matrix[j][i] = 1
                matrix[i][j] = 1
            cursor += 1

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
        return True
    return False

def calculate_einvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

def calculate_score(eigenvalues):
    score = sum(abs(ev - np.round(ev)) for ev in eigenvalues)
    return score

def add_edge(matrix, max_k, max_n):

    current_n = len(matrix)
    new_idx = current_n
    existing_edges = [(i, j) for i in range(current_n) for j in range(i) if matrix[i][j] == 1]
    avaiable_k = max_k - len(existing_edges)
    avaiable_to_use_k = avaiable_k - (max_n-current_n) +1
    max_deg = min(current_n, avaiable_to_use_k)
    final_matrix = []
    max_score = 0

    for deg in range(1 if current_n<(max_n-1) else max_deg, max_deg+1):
        for neighbors in itertools.combinations(range(current_n), deg):

            new_matrix = [row + [0] for row in matrix]
            new_matrix.append([0]*(current_n+1))
            new_k = []
            for neighbor in neighbors:

                new_matrix[new_idx][neighbor] = 1
                new_matrix[neighbor][new_idx] = 1

                if(abs((current_n -1) - max_score) >= abs((current_n - 1) - calculate_score(calculate_einvalues(new_matrix)) and dfs(new_matrix))):
                    final_matrix = new_matrix
                    max_score = calculate_score(calculate_einvalues(new_matrix))

    return final_matrix

if __name__ == "__main__":

    n = int(sys.argv[1]) if (len(sys.argv)>1) else 15
    k = int(sys.argv[2]) if (len(sys.argv)>2) else 78

    best_matrix = None
    best_matrix_score = 0
    graphn_9 = "H~~~~~~"
    matrix = convert_to_adjacency_matrix(graphn_9)

    while len(matrix) < n:
        matrix = add_edge(matrix, k, n)

    if matrix:
        print(convert_to_graph6(matrix))
