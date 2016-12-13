from __future__ import division

import networkx as nx
import community 

sigma =1

def minimum_of_float_list(liste):
	minimum=0
	for i in liste:
		print i
		if float(i)<minimum:
			minimum=float(i)
			print minimum
	return minimum
# get cluster in a graph 
def get_community(G,nb_cluster):
	part = community.best_partition(G)
	liste=[]
	for node, cluster in part.items():
		if cluster == nb_cluster:
			liste.append(node)
	return G.subgraph(liste)

def get_key_of_value(dict,value):
	keys=[]
	for ele in dict.keys():
		if dict[ele] == value:
			keys.append(ele)
	return keys
def get_clusters_node(part,cluster):
	vertex=[]
	for node in part.keys():
		if part[node] == cluster:
			vertex.append(node)
	return vertex
        
def Graclus_centers( G  ):
	seeds=[]
	part = community.best_partition(G)
	
	clusters =[]
	
	for val in part.values(): 
		if val in clusters: 
			continue
		else:
			clusters.append(val)
		print clusters
    
	for cluster in clusters:
		distances ={}
		subGraph=get_community(G,cluster)
		linksCi_Ci=subGraph.number_of_edges()
		print linksCi_Ci
		degCi=sum(G.degree(subGraph.nodes()).values())
		print degCi
		print(" dans le cluster %d  " % cluster)
		for vertex in get_clusters_node(part,cluster):
		
			degV=subGraph.degree(vertex)
			
			linksV_Ci=len(G.neighbors(vertex))
			
			print("pour le vertex %d  " % vertex)
			distances.update({vertex: (-2*linksV_Ci/degV*degCi)+(linksCi_Ci/degCi**2)+(sigma/degV)-(sigma/degCi)})
			print distances
		print(" dans le cluster %d  la distance minimal est de %f" % (cluster,min( distances.values())))

		seeds.append(get_key_of_value(distances,min( distances.values()))[0])
	return seeds
