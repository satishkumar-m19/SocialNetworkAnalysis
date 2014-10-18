import networkx as nx
import random as rand
import itertools
import bisect
from collections import deque

def bfs(g,source):
    iterator_for_neighbors = g.neighbors_iter
    visited=set([0])
    queue = deque([(source, iterator_for_neighbors(source))])
    selected_edges = []
    while queue:
        parent, children = queue[0]
        try:
            child = next(children)
            if child not in visited:
                #print parent,child
                selected_edges.append((parent,child))
                visited.add(child)
                queue.append((child,iterator_for_neighbors(child)))
        except:
            queue.popleft()
    return selected_edges

def pivot_random_walk(g,source,number_of_iteration):
    selected_edges = []
    curr_node_value = source
    for i in range(number_of_iteration):
        next_node_index = rand.randrange(1,g.degree([curr_node_value])[curr_node_value]+1,1)
        next_node_value =  g.neighbors(curr_node_value)[next_node_index-1]
        #print curr_node_value,next_node_value
        selected_edges.append((curr_node_value,next_node_value))
        curr_node_value = next_node_value
    display_graph(selected_edges)

def weighted_independence(g,number_of_iteration):
    n = len(g)
    cum_weights = [0]*n
    tot_weight = 0
    nx.draw(g)
    size = 10
    weights = g.degree()
    for i,v in enumerate(g):
        tot_weight += weights[v]
        cum_weights[i] = tot_weight
    #print cum_weights
    for c in itertools.count():
        if c==size:
            break
        rand_var = rand.random()
        #print rand_var*tot_weight
        i = bisect.bisect_right(cum_weights, rand_var * tot_weight)
        #print i
        print g.nodes()[i]

def display_graph(list_of_edges):
    g_result = nx.Graph()
    g_result.add_edges_from(list_of_edges)
    nx.draw(g_result)   

def main():
    g = nx.Graph()
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,32]
    edges= [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 10), (1, 2), (1, 3), (1, 7),
            (2, 3), (2, 32), (2, 7), (2, 8), (2, 9),(3, 7),(4, 10), (4, 6),(5, 10), (5, 6)]
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    source = 0
    
    #the default method delivered from the networkx
    print list(nx.bfs_edges(g,0))
    
    #call to the bfs
    final_edges = bfs(g,source)
    display_graph(final_edges)
    print "bfs done"
    #Call to the pivot random walk
    pivot_random_walk(g,source,20)
    print "pivot random done"
    #Call to the pivot random walk
    g= nx.davis_southern_women_graph()
    weighted_independence(g,25)
    print "completion"


if __name__ == '__main__':
    print "Start of the program "
    main()
