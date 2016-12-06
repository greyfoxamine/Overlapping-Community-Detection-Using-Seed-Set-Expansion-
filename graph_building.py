
import matplotlib.pyplot as plt
import networkx as nx
import sys

def file_graph_show( G ):
	print "\rStructuration d'un graph..."
	nx.draw(G)  # networkx draw()
	print "\rDessin du graph...."
	plt.draw()  # pyplot draw()
	print "\rAffichage du graph"
	plt.show()
def file_graph_building( path ):
   
	G=nx.Graph()
	f = open(sys.argv[1],'r')
	lignes  = f.readlines()
	f.close()
	i=0
	tab=range(len(lignes))


	for ligne in lignes:
    		sys.stdout.write("\r%d%%" % tab[i])
    		sys.stdout.flush()

    		ligne=ligne.replace('\n', '')
    		ligne=ligne.split(' ', 1 )
    		G.add_edges_from([(ligne[0],ligne[1])])
    		i=i+1
    
  
   	return G
   



