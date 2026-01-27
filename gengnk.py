import sys
import random
import networkx as nx
import time
 
 
if __name__ == "__main__":
  n = int(sys.argv[1]) if (len(sys.argv)>1) else 5
  k = int(sys.argv[2]) if (len(sys.argv)>2) else 3
  rep = int(sys.argv[3]) if (len(sys.argv)>3) else 10000
  if (len(sys.argv)>4):
    random.seed(int(sys.argv[4])) 
  start = time.perf_counter() 
  for _ in range(rep):
    #G = nx.dense_gnm_random_graph(n,k)
    G = nx.gnm_random_graph(n,k)
    print(nx.to_graph6_bytes(G,header=False).decode("UTF-8"),end="")
  stop = time.perf_counter()
  #print('Time [sec]:',stop-start)
  sys.stderr.write('Time [sec]: {dt}'.format(dt = stop-start))
