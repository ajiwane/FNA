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
measures=["page_with_weight","page_without_weight","eigen_with_weight","eigen_without_weight","degree_with_weight","degree_without_weight"]
start_nodes = [[1641,50,3381,260,334],[100,0,3381,334,399],[2160,2416,2553,2172,2458],[2220,2416,2553,2458,2187],[100,2300,1844,2494,1641],[100,2300,1844,2494,1641]]

filename = "weights.gml"

fb = Graph.Read_GML(filename)

vs_obj = fb.vs
not_infected = []
for n in vs_obj:
	not_infected.append(int(n["id"]))

#probs = [0.3,0.2,0.1.0.05] 
#probs=[0.1]

infected = []
cantinfectmore = []
consider_weight = False

f_rand = open("randoms1.txt",'r')

def reset():
	global infected
	global not_infected
	global cantinfectmore
	global fb
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

'''
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
'''

def siwithstartnodes():
	i=0
	for measure in measures:
		print "********** STARTING FOR MEASURE "+measure+" **************"
		global infected
		global not_infected
		global consider_weight
		if(consider_weight):
			consider_weight = False
		else:
			consider_weight = True
		reset()
		filename = "sivalues/copyfiles/si_vals_"+measure+".txt"
		f = open(filename,'w')
		infected = [start_nodes[i]]
		for startnode in start_nodes[i]:
			not_infected.remove(startnode)
			
		if(consider_weight):
			sihelper(-1)
		else:
			sihelper(0.1)
		
		total_infected = 0
		for t in infected:
			f.write(str(len(t))+",")
			total_infected+=len(t)
			liststr = str(t)
			liststr = liststr.strip('[]')
			f.write(liststr+"\n")
		f.close()
		i+=1

siwithstartnodes()