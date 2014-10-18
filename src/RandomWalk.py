import random as rand
import networkx as nx
from collections import deque

g = nx.Graph()
nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,32]
edges= [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 10), (1, 2), (1, 3), (1, 7),(2, 3), (2, 32), (2, 7), (2, 8), (2, 9),(3, 7),(4, 10), (4, 6),(5, 10), (5, 6)]
g.add_nodes_from(nodes)
g.add_edges_from(edges)
source = 0
number_of_iteration = 10

# current_node_index = rand.randrange(g.degree([source])+1)
deg = g.degree([source])[source]
print deg
