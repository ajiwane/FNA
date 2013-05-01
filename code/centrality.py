from igraph import *
from numpy import *

graphs = ['weights.gml']
file = ['centrality.csv']

for i in range(len(graphs)): 
	measures = []
	g = Graph.Read_GML(graphs[i])
	edges = g.es()
	w = []
	for e in edges:
		w.append(e["weight"])
	f = open(file[i] , 'w')
	# measures.append(g.pagerank(weights = w)) 
	measures.append(g.authority_score(weights = w))
	# measures.append(g.eigenvector_centrality(weights = w))
	measures.append(g.betweenness(weights = w))
	measures.append(g.closeness(weights = w))
	# measures.append(g.degree())
	# eigenvalues
	# lap = g.laplacian()
	# eignvals, eignvecs = linalg.eig(lap)
	# sorted_eignval = sort(eignvals)
	# lambda2 = sorted_eignval[1]
	# lambdan = sorted_eignval[len(sorted_eignval)-1]
	# ind2 = list(eignvals).index(lambda2)
	# lambda2_vec= eignvecs[ind2]
	# indn = list(eignvals).index(lambdan)
	# lambdan_vec= eignvecs[indn]
	# measures.append(lambda2_vec)
	# measures.append(lambdan_vec)
	# f.write("pagerank,authority_score,eigenvector_centrality,betweenness,closeness,degree,lambda 2,lambda n\n")
	f.write("authority_score,betweenness,closeness\n")
	for j in range(len(measures[0])):
		for k in range(len(measures)):
			f.write("%s," % measures[k][j])
		f.write("\n")
	f.close()