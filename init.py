
import matplotlib.pyplot as plt
import networkx as nx
import sys
import graph_building as gb
import community 
import Graclus_centers as gc


# filtering phase phase Remove unimportant regions of the graph
#Trivially separable from the rest of the graph
#Do not participate in overlapping clustering
#Our filtering procedure
#Remove all single-edge biconnected components (remain connected after
#removing any vertex and its adjacent edges)
#Compute the largest connected component

def filtering_phase( G ):
	
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
#gb.file_graph_show(G,1).show()


print "filtering_phase processing...."
G= filtering_phase( G  )
print(nx.info(G))

#gb.file_graph_show(G,2).show()

#print "seeding phase"

seeds= gc.Graclus_centers( G  )
print seeds
#print gc.minimum_of_float_list(seeds.values())

#degCi=sum(G.degree(G.nodes()))
#part = community.best_partition(G,resolution=2)
#values = [part.get(node) for node in G.nodes()]
#print values
#nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
#plt.show()


