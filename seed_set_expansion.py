from __future__ import division

import random as rdm

import networkx as nx
def seed_set_expansion(G,seeds):
	#star random walk
	expansion ={} 
	compteur= 0 #Start execution counter 
	execution = 0
	for seed in seeds:
		
		vertexid = seed
		VisitedVertex = {}
		
		#Execute the random walk with size 10000 (10000 steps)
		while compteur < G.number_of_nodes()/len(seeds):
			#Accumulate the amount of times each vertex is visited
			if vertexid in VisitedVertex:
				VisitedVertex[vertexid] += 1
			else:
				VisitedVertex[vertexid] = 1
			#Visualize the vertex neighborhood
			Vertex_Neighbors = G.neighbors(vertexid)
			#Choose a vertex from the vertex neighborhood to start the next random walk
			vertexid = rdm.choice(Vertex_Neighbors)
			compteur = compteur + 1
		mostvisited = sorted(VisitedVertex, key = VisitedVertex.get,reverse = True)
		expansion.update({seed: mostvisited})	
		compteur = 0

	return expansion
def color_building_list(G,expansion):
	partition ={}

	
	valeur=0
	for liste_value in expansion.values():
		for node in liste_value:
			partition.update({node: valeur})
		valeur = valeur+1
	
	values = [partition.get(node) for node in G.nodes()]
	print values
	for i, val in enumerate(values):
		if val == None:
			values[i]=values[i-1]
	return values
			 