from igraph import *
import numpy as np
import math
import random 
import time 

'''
filename = "randoms.txt"
f = open(filename,'w')
for i in range(1000000):
	f.write(str(round(random.random(),4))+"\n")
f.close()
'''


filename = "weights.gml"

fb = Graph.Read_GML("facebook/"+filename)

vs_obj = fb.vs
not_infected = []
for n in vs_obj:
	not_infected.append(int(n["id"]))

infected = []
cantinfectmore = []

es = fb.es
print (len(es.select(_source=2)))
print(es.select(_source=2)[0]["weight"])


def cascadehelper():
	global infected
	global not_infected
	global fb
	global cantinfectmore
	f_rand = open("randoms.txt",'r')

	while(len(not_infected)>0):
		print "***** Starting new timestamp"
		print infected
		got_inf = []
		for t_infe in infected:
			for node in t_infe:
				if(node not in cantinfectmore):
					print "infecting neighbors of node " + str(node)
					edges = fb.es.select(_source=node)
					nbrs = []
					wts = []
					for e in edges:
						#print e.target
						nbrs.append(e.target)
						wts.append(e["weight"])
					index = 0
					nodestopsinfet = True
					for nbr in nbrs:
						if(nbr in not_infected):
							nodestopsinfet = False
							rand = f_rand.readline()
							rand = rand.strip()
							rand = float(rand)
							if(rand>wts[index]):
								print "got infected : node " + str(nbr)
								not_infected.remove(nbr)
								got_inf.append(nbr)
						index+=1
					if(nodestopsinfet):
						cantinfectmore.append(node)
		infected.append(got_inf)
		print "sleeping.."
		time.sleep(10)
	f_rand.close()


def cascade(startnode):
	global infected
	global not_infected
	infected = [[startnode]]
	not_infected.remove(startnode)
	cascadehelper()

cascade(2160)

filename = "cascade_vals_weighted.txt"
f = open(filename,'w')

for t in infected:
	f.write(str(len(t))+",")
	liststr = str(t)
	liststr = liststr.strip('[]')
	f.write(liststr+"\n")
f.close()
