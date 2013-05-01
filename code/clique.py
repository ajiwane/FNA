# Creates a GML file from .csv file without edge value
from operator import itemgetter
from igraph import *

graphs = "weights.gml"
g = Graph.Read_GML(graphs)
# g.vs(clique=2)["color"] = "green"
print "CLIQUES"
x = g.clique_number()
print x
# print g.cliques()