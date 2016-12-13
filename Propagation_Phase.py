import matplotlib.pyplot as plt
import networkx as nx
import sys

def difference(S, R):
    #R = G.copy()
    #R.remove_nodes_from(n for n in G if n in H)
    #return R
    print " prolongation phase processing ..."
    DIF=nx.Graph()
    for edge in S.edges_iter():
        if not R.has_edge(edge[0],edge[1]):
            DIF.add_edge(edge[0],edge[1])
  
    for edge in DIF.edges_iter():
        R.add_edge(edge[0],edge[1])
    print "after prolongation phase done"
    return R