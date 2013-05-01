from igraph import *
import numpy as np
import math

fb = Graph.Read_GML("./facebook/master.gml")
print Graph.summary(fb)
adj_mat = fb.get_adjacency()
vs_obj = fb.vs
nodes = []
for n in vs_obj:
	nodes.append(int(n["id"]))
print len(nodes)

#print adj

edges = fb.get_edgelist()
print len(edges)
#print edges[0].__class__.__name__

def norm(u):
	return (math.sqrt(np.dot(u,u)))

def calcos(u,v):
	cos = np.dot(u,v)/norm(u)/norm(v)
	return cos

#print calcos([1,2,1,1],[1,2,1,3])

max_cos_val = 0.0
sim_node1 = -1
sim_node2 = -1
print len(adj_mat._get_data())

def calcosvals():
	global max_cos_val
	global sim_node2
	global sim_node1
	filename = "master_weights.csv"
	fin = open(filename,'w')

	for edge in edges:
		#print edge
		n1 = edge[0]
		n2 = edge[1]
		print "calculating for nodes " + str(n1) + "," +str(n2)
		u = adj_mat[n1]
		v = adj_mat[n2]
		cos = calcos(u,v)
		print cos
		if(cos>max_cos_val):
			max_cos_val = cos
			sim_node1 = n1
			sim_node2 = n2
		fin.write(str(n1)+","+str(n2)+","+str(cos)+"\n")

calcosvals()
print "MAX COS VALUE:"
print max_cos_val
print sim_node1
print sim_node2
