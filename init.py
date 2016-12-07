
import matplotlib.pyplot as plt
import networkx as nx
import sys
import graph_building as gb

G=gb.file_graph_building( sys.argv[1] )
gb.file_graph_show(G,1)
print nx.number_of_nodes(G)
node_a_supprimer = [];
for node in G.nodes_iter(data=False):
	if len(G.neighbors(node)) <= 1:
		node_a_supprimer.append(node)


for element in node_a_supprimer:
	G.remove_node(element)

print nx.number_of_nodes(G)
gb.file_graph_show(G,2).show()
