# Creates a GML file from .csv file without edge value
from operator import itemgetter

f = open("master.gml","w")
g = open("master.csv","r")

data = []
node = []
f.write("Formatted by Shubham Agrawal on Sat April 20\ngraph\n[\n\tdirected 0\n")

for line in g:
	line = line.strip("\n")
	l = line.split(",")
	l[0] = int(l[0])
	l[1] = int(l[1])
	if l not in data:
		data.append(l)
	if l[0] not in node:
		node.append(l[0])
	if l[1] not in node:
		node.append(l[1])
		
node.sort()	
		
print len(data), len(node)

for n in node:
	f.write("\tnode\n\t[\n\t\tid "+str(node.index(n))+"\n\t]\n")
print "Nodes done"
for d in data:
	f.write("\tedge\n\t[\n\t\tsource "+str(node.index(d[0]))+"\n\t\ttarget "+str(node.index(d[1]))+"\n\t]\n")

f.write("]")
	
f.close()
g.close()