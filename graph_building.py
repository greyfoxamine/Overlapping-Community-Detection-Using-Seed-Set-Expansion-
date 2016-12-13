
import matplotlib.pyplot as plt
import networkx as nx
import sys

def file_graph_show( g,i ):
	plt.figure(i)
	
	sp=nx.spring_layout(g)

	plt.axis('off')

	nx.draw_networkx(g,pos=sp,with_labels=False,node_size=35)
	return plt
	
def file_graph_building( path ):
   
	g=nx.read_edgelist(path,create_using=nx.Graph(),nodetype=int)

	print nx.info(g)
	return g

	
   





