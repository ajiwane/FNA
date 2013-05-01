# Creates a combined edge list from all the edge lists
# Makes the graph UNDIRECTED
from operator import itemgetter

m = open("master.csv","w")
ego = [0,686,698,1684,1912,3437,3980,107,348,414]

data = []
dataCopy = []
for e in ego:
	input = str(e)+".csv"
	g = open(input,"r")
	print "Started", e

	for line in g:
		line = line.strip("\n")
		l = line.split(",")
		l[0] = int(l[0])
		l[1] = int(l[1])
		x = []
		x.append(l[1])
		x.append(l[0])
		if l not in data and x not in data:
			data.append(l)
		
data.sort(key=itemgetter(1))	
data.sort(key=itemgetter(0))
# print data
for d in data:
	m.write(str(d[0])+","+str(d[1])+"\n")
m.close()
g.close()