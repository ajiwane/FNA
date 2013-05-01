from igraph import *
import numpy as np
import math
import random 
import time 
import copy

'''
filename = "randoms.txt"
f = open(filename,'w')
for i in range(1000000):
	f.write(str(round(random.random(),4))+"\n")
f.close()
'''

start_nodes_withoutwt = [3381,1868,100]
start_nodes_withwt = [1641,1868,2160,100]

filename = "weights.gml"

fb = Graph.Read_GML("facebook/"+filename)

vs_obj = fb.vs
not_infected = []
for n in vs_obj:
	not_infected.append(int(n["id"]))

infected = []
cantinfectmore = []
timeperiod = 3

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

def sirhelper():
	global timeperiod
	global infected
	global not_infected
	global fb
	global cantinfectmore
	f_rand = open("randoms.txt",'r')
	currtime = 1
	breakcount=0
	infected_copy = []
	while(len(not_infected)>0):
		print "***** Starting new timestamp"
		#print infected
		if(currtime>timeperiod):
			infected_copy = copy.deepcopy(infected)
			for i in range(currtime-timeperiod):
				print "lneght of infected copy : "+ str(len(infected_copy))
				print "i:" +str(i)
				infected_copy.pop(0)
		else:
			infected_copy = copy.deepcopy(infected)
		got_inf = []
		for t_infe in infected_copy:
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
								w = 0.2
							if(rand<w):
								print "got infected : node " + str(nbr)
								not_infected.remove(nbr)
								got_inf.append(nbr)
						index+=1
					if(nodestopsinfet):
						cantinfectmore.append(node)
		if(len(got_inf)==0):
			breakcount+=1
		else:
			breakcount=0
		if(breakcount==3):
			break
		infected.append(got_inf)
		print "sleeping.."
		time.sleep(2)
		currtime+=1
	f_rand.close()


def sir(startnode):
	global infected
	global not_infected
	infected = [[startnode]]
	not_infected.remove(startnode)
	sirhelper()
	while(len(not_infected)>0):
		infected.append([])
		nextindex = random.randrange(len(not_infected))
		infected.append([not_infected[nextindex]])
		not_infected.remove(not_infected[nextindex])
		sirhelper()

#sir(2160)
consider_weight = False

for sn in start_nodes_withoutwt:

	print "********* WITHOUT WEIGHT startnode= "+str(sn)+" **************"
	reset()
	sir(sn)
	filename = "sir_vals_withoutweighted_"+str(sn)+".txt"
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

for sn in start_nodes_withwt:

	print "********* WITH WEIGHT startnode= "+str(sn)+" **************"
	reset()
	sir(sn)
	filename = "sir_vals_withweighted_"+str(sn)+".txt"
	f = open(filename,'w')

	total_infected = 0
	for t in infected:
		f.write(str(len(t))+",")
		total_infected+=len(t)
		liststr = str(t)
		liststr = liststr.strip('[]')
		f.write(liststr+"\n")
	f.close()