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

start_nodes_withoutwt = [3381,1868,100]
start_nodes_withwt = [1641,2160,100]

filename = "weights.gml"

fb = Graph.Read_GML(filename)

vs_obj = fb.vs
not_infected = []
for n in vs_obj:
	not_infected.append(int(n["id"]))

probs = [0.5,0.3,0.2,0.1] 

infected = []
cantinfectmore = []
f_rand = open("randoms1.txt",'r')

def reset():
	global infected
	global not_infected
	global cantinfectmore
	global fb
	global consider_weight
	cantinfectmore = []
	infected = []
	not_infected = []
	vs_obj = fb.vs
	for n in vs_obj:
		not_infected.append(int(n["id"]))

def sihelper(prob):
	global infected
	global not_infected
	global fb
	global cantinfectmore
	global consider_weight
	global f_rand
	while(len(not_infected)>0):
		print "***** Starting new timestamp"
		#print infected
		got_inf = []
		for t_infe in infected:
			for node in t_infe:
				if(node not in cantinfectmore):
					#print "infecting neighbors of node " + str(node)

					edges = fb.es.select(_source=node)
					nbrs = []
					wts = []
					for e in edges:
						#print e.target
						nbrs.append(e.target)
						wts.append(e["weight"])

					edges = fb.es.select(_target=node)
					for e in edges:
						#print e.target
						nbrs.append(e.source)
						wts.append(e["weight"])

					index = 0
					nodestopsinfet = True
					#print "neigbors: "
					#print nbrs
					for nbr in nbrs:
						if(nbr in not_infected):
							nodestopsinfet = False
							rand = f_rand.readline()
							rand = rand.strip()
							rand = float(rand)
							if(consider_weight):
								w = wts[index]
							else:
								w = prob
							if(rand<w):
								print "got infected : node " + str(nbr)
								not_infected.remove(nbr)
								got_inf.append(nbr)
						index+=1
					if(nodestopsinfet):
						cantinfectmore.append(node)
		if(len(got_inf)==0):
			break
		infected.append(got_inf)
		print "sleeping.."
		time.sleep(2)
	#f_rand.close()


def si(startnode,prob):
	global infected
	global not_infected
	infected = [[startnode]]
	not_infected.remove(startnode)
	sihelper(prob)
	while(len(not_infected)>0):
		infected.append([])
		nextindex = random.randrange(len(not_infected))
		infected.append([not_infected[nextindex]])
		not_infected.remove(not_infected[nextindex])
		sihelper(prob)

#si(2160)
consider_weight = False

for sn in start_nodes_withoutwt:

	for prob in probs:
		print "********* WITHOUT WEIGHT startnode= "+str(sn)+" **************"
		reset()
		si(sn,prob)
		filename = "sivalues/si_vals_"+str(prob)+"_"+str(sn)+".txt"
		f = open(filename,'w')

		total_infected = 0
		for t in infected:
			f.write(str(len(t))+",")
			total_infected+=len(t)
			liststr = str(t)
			liststr = liststr.strip('[]')
			f.write(liststr+"\n")
		f.close()

consider_weight = True

'''
for sn in start_nodes_withwt:

	print "********* WITH WEIGHT startnode= "+str(sn)+" **************"
	reset()
	si(sn)
	filename = "sivalues/si_vals_withweighted_"+str(sn)+".txt"
	f = open(filename,'w')

	total_infected = 0
	for t in infected:
		f.write(str(len(t))+",")
		total_infected+=len(t)
		liststr = str(t)
		liststr = liststr.strip('[]')
		f.write(liststr+"\n")
	f.close()
'''