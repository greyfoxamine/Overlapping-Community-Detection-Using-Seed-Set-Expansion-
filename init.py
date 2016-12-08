
import matplotlib.pyplot as plt
import networkx as nx
import sys
import graph_building as gb
import community


# filtering phase phase Remove unimportant regions of the graph
#Trivially separable from the rest of the graph
#Do not participate in overlapping clustering
#Our filtering procedure
#Remove all single-edge biconnected components (remain connected after
#removing any vertex and its adjacent edges)
#Compute the largest connected component

def filtering_phase( G ):
	print "filtering_phase processing...."
	liste=[]
	nb_node=G.nodes_iter(data=False)
	
	for node in nb_node:
		if len(G.neighbors(node)) <= 1:
			liste.append(node)

	
	if(len(liste) !=0):
		G.remove_node(liste[0])
		
		return filtering_phase(G)
 	return G


	
G=gb.file_graph_building( sys.argv[1] )
gb.file_graph_show(G,1)
print(nx.info(G))

G= filtering_phase( G  )
print(nx.info(G))

gb.file_graph_show(G,2).show()

