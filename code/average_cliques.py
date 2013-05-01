from igraph import *

graphs = ['weights.gml']
file = ['cliques_data.txt','average_cliques.csv']
measures = [[],[],[],[],[]]

def getmeasures():	
	for i in range(len(graphs)): 
		global measures
		g = Graph.Read_GML(graphs[i])
		edges = g.es()
		w = []
		for e in edges:
			w.append(e["weight"])
		measures[0] = g.pagerank(weights = w) 
		measures[1] = g.pagerank() 
		measures[2] = g.eigenvector_centrality(weights = w) 
		measures[3] = g.eigenvector_centrality() 
		measures[4] = g.degree()

def calaverages():
	global measures
	global file
	f = open(file[0],'r')
	f_out = open(file[1],'w')
	line = f.readline()
	f_out.write("clique size,pagerank with weight,pagerank without weight,eigen with weight, eigen without weight,degree\n")
	while line:
		line = line.strip()
		line = line.split(",")
		size = int(line[0])
		nodes = line[1:]
		avg=[0.0]*5
		for n in nodes:
			n = int(n)
			for i in range(5):
				avg[i]+=measures[i][n]
		avg = [k/size for k in avg]

		f_out.write(str(size)+",")
		for i in range(5):
			f_out.write(str(avg[i])+",")
		f_out.write("\n")
		line = f.readline()
	f_out.close()
	f.close()

getmeasures()
print measures[0]
#calaverages()