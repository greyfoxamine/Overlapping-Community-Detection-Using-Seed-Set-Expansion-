import networkx as nx
import community 

def get_clusters_node(part,cluster):
	vertex=[]
	for node in part.keys():
		if part[node] == cluster:
			vertex.append(node)
	return vertex

def SpreadHubs(G):
	part = community.best_partition(G)
	clusters =[]
	degree=0
	for val in part.values(): 
		if val in clusters: 
			continue
    	else:
    		clusters.append(val)
    for cluster in clusters:
		for vertex in get_clusters_node(part,cluster):
			
