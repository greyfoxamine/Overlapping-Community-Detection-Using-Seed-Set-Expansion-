# -*-coding:utf-8 -*
import matplotlib.pyplot as plt
import networkx as nx
import sys
import graph_building as gb
import community 
import Graclus_centers as gc
import seed_set_expansion as sse
import Propagation_Phase as pp
import time


# filtering phase phase Remove unimportant regions of the graph
#Trivially separable from the rest of the graph
#Do not participate in overlapping clustering
#Our filtering procedure
#Remove all single-edge biconnected components (remain connected after
#removing any vertex and its adjacent edges)
#Compute the largest connected component

mon_fichier = open("com1.txt", "w") # Argh j'ai tout écrasé !






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


t = time.time()
print "filtering_phase processing...."


G= filtering_phase( G  )
print len(G.nodes())


#mon_fichier.write("Filtering phase in :"+repr(time.time()-t)+"\n")

print "filtering_phase done!"

t = time.time()

print "seeding phase"

seeds= gc.Graclus_centers( G  )

#mon_fichier.write("seeding phase in :"+repr(time.time()-t)+"\n")
print "seeding phase done!"

t = time.time()

print "seed set expansion phase"

expansion=sse.seed_set_expansion(G,seeds)
#mon_fichier.write("seed set expansion  phase in :"+repr(time.time()-t)+"\n")
print "seedingset expansion phase done!"

#seeds= gc.Graclus_centers( G  )
#print seeds
#print gc.minimum_of_float_list(seeds.values())

#degCi=sum(G.degree(G.nodes()))


#print G.nodes()
#print G.edges()
#G=nx.to_numpy_matrix(G, nodelist=G.nodes())
#print G
print "Graph building with coloring community"



#values=sse.color_building_list(G,expansion)
#nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
for valeur in expansion.values():
	string=""
	for element in valeur:
		string=string+str(element)+" "
	mon_fichier.write(string.rstrip())
	mon_fichier.write("\n")
	


#plt.figure(0)
	
#sp=nx.spring_layout(G)

#plt.axis('off')

#nx.draw_networkx(G,pos=sp,with_labels=False,node_size=35)

print "building graph  done!"
mon_fichier.close()
#plt.show()

mon_fichier = open("com2.txt", "w") # Argh j'ai tout écrasé !

G=gb.file_graph_building( sys.argv[1] )

part = community.best_partition(G)
	
clusters =[]
	
for val in part.values(): 
	if val in clusters: 
		continue
	else:
		clusters.append(val)
print clusters

for cluster in clusters:
	string =""
	for element in gc.get_clusters_node(part,cluster):
		string=string+str(element)+" "
	mon_fichier.write(string.rstrip())
	mon_fichier.write("\n")


mon_fichier.close()
