#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//compilation gcc random.c -o random
//usage: ./random.c 15 27 1000000

void dfsRec(char *adj, int n, int *visited, int s) {
    visited[s] = 1;

    for (int i = 0; i < n; i++) {
        if (adj[s * n + i] && visited[i] == 0)
            dfsRec(adj, n, visited, i);
    }

}

bool dfs(int *adj, int n) {
    int visited[n];
    memset(visited, 0, n * sizeof(int));
    int idx = 0;
    dfsRec(adj, n, visited, 0);
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            return false;
        }
    }
    return true;
}
void printgraph6(int n, char *adj){
    if (n <= 0 || n > 62) {
        return;
    }else{
        putchar(63 + n);
    }

    int bit_count = 0;
    unsigned char current_byte = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            current_byte <<= 1;
            if(adj[j * n + i]) {
                current_byte |= 1;
            }
            bit_count++;
            if (bit_count == 6) {
                putchar(63 + current_byte);
                bit_count = 0;
                current_byte = 0;
            }
        }
    }
    if (bit_count > 0) {
        current_byte <<= (6 - bit_count);
        putchar(63 + current_byte);
    }
    putchar('\n');
}

int main(int argc, char *argv[]) {

    int n = (argc > 1) ? atoi(argv[1]) : 3;
    int k = (argc > 2) ? atoi(argv[2]) : 5;
    int rep = (argc > 3) ? atoi(argv[3]) : 1000;
    if (argc > 4) {
        srand(atoi(argv[4]));
    } else {
        srand(time(NULL));
    }
    char *adj = malloc(n * n * sizeof(char));
    clock_t start, end;
    start = clock();
    for (int r = 0; r < rep; r++) {
        bool connected = false;

        while (!connected) {
            memset(adj, 0, n * n * sizeof(char));
            int k_added = 0;

            while(k_added < k) {
                int u = rand() % n;
                int v = rand() % n;
                if (u != v && !adj[u * n + v]) {
                    adj[u * n + v] = 1;
                    adj[v * n + u] = 1;
                    k_added++;
                }
            }
            connected = dfs(adj, n);
        }
        printgraph6(n, adj);
    }
    end = clock();
    free(adj);
    fprintf(stderr, "Time taken: %lf seconds\n", ((double)(end - start)) / CLOCKS_PER_SEC);
    return 0;
}