#example of usage: python greedysub9.py 78 15
#it use a 9 nodes complete graph and mutate it node by node to kepp the closest spectral radius to n-1. 
#finally displaying in graph6 format

import random
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

def calculate_spectral_radius(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    spectral_radius = max(abs(ev) for ev in eigenvalues)
    return spectral_radius


def add_edge(matrix, max_k, max_n):

    cuurent_n = len(matrix)
    new_idx = cuurent_n
    existing_edges = [(i, j) for i in range(cuurent_n) for j in range(i) if matrix[i][j] == 1]
    avaiable_k = max_k - len(existing_edges)
    avaiable_to_use_k = avaiable_k - (max_n-cuurent_n) +1
    max_deg = min(cuurent_n, avaiable_to_use_k)
    final_matrix = []
    max_score = 0

    if (cuurent_n<(max_n-1)):
        pass
    else:
        print("temp: ", len(existing_edges), cuurent_n, max_n, max_deg)

    for deg in range(1 if cuurent_n<(max_n-1) else max_deg, max_deg+1):
        for neighbors in itertools.combinations(range(cuurent_n), deg):

            new_matrix = [row + [0] for row in matrix]
            new_matrix.append([0]*(cuurent_n+1))
            new_k = []
            for neighbor in neighbors:
                
                new_matrix[new_idx][neighbor] = 1
                new_matrix[neighbor][new_idx] = 1

                if(max_score <= calculate_spectral_radius(new_matrix) and dfs(new_matrix)):
                    final_matrix = new_matrix
                    max_score = calculate_spectral_radius(new_matrix)
    
    return final_matrix
 
if __name__ == "__main__":

    rep = int(sys.argv[1]) if (len(sys.argv)>1) else 10000
    k = int(sys.argv[2]) if (len(sys.argv)>2) else 78
    n = int(sys.argv[3]) if (len(sys.argv)>3) else 15
    iterations = int(sys.argv[4]) if (len(sys.argv)>4) else 10000
    best_matrix = None
    best_matrix_score = 0

    graphn_9 = "H~~~~~~"

    print(convert_to_adjacency_matrix(graphn_9))

    matrix = convert_to_adjacency_matrix(graphn_9)

    while len(matrix) < n:

        matrix = add_edge(matrix, k, n)

    if matrix:
        print("result: ", convert_to_graph6(matrix), "k:", len([(i, j) for i in range(len(matrix)) for j in range(i) if matrix[i][j] == 1]))
