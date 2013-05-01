from igraph import *

graphs = ['weights.gml']
node = [100,1868,2160,3381,1641]
for i in range(len(graphs)): 
	measures = [[],[],[],[],[]]
	g = Graph.Read_GML(graphs[i])
	layout = g.layout_grid_fruchterman_reingold()
	print layout.__class__
	# for n in node:
		# g.vs.select(n)["color"] = "blue"
		# g.vs.select(n)["vertex_size"] = 10
	# Graph.write_svg(g, "plot1.svg", layout = layout, colors='red', width=1000, height=600, shapes='1', vertex_size=2, font_size=4)