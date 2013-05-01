from igraph import *
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
#measures=["page_with_weight","page_without_weight","eigen_with_weight","eigen_without_weight","degree_with_weight","degree_without_weight"]
#start_nodes = [[1641,50,3381,260,334],[100,0,3381,334,399],[2160,2416,2553,2172,2458],[2220,2416,2553,2458,2187],[100,2300,1844,2494,1641],[100,2300,1844,2494,1641]]
measures=["degree_with_weight"]
start_nodes = [[100,2300,1844,2494,1641]]

filename = "weights.gml"

fb = Graph.Read_GML(filename)

vs_obj = fb.vs
not_infected = []
for n in vs_obj:
	not_infected.append(int(n["id"]))

#probs = [0.3,0.2,0.1.0.05] 
#probs=[0.1]
not_infected_maincopy=[]
not_infected_maincopy=copy.deepcopy(not_infected)
infected = []

cantinfectmore = []
consider_weight = False
timeperiod = 3

f_rand = open("randoms1.txt",'r')

def reset():
	global infected
	global not_infected
	global cantinfectmore
	global fb
	global not_infected_maincopy
	cantinfectmore = []
	infected = []
	not_infected = copy.deepcopy(not_infected_maincopy)
	

def sirhelper(prob):
	global timeperiod
	global infected
	global not_infected
	global fb
	global cantinfectmore
	global f_rand
	currtime = 1
	breakcount=0
	degrading_factor = 0.75

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
		lenthofinfected = len(infected_copy)
		infecting_index=1
		
		for t_infe in infected_copy:
			degrade = math.pow(degrading_factor,lenthofinfected-infecting_index)
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
								w = wts[index]*degrade
							else:
								w = prob
							if(rand<w):
								#print "got infected : node " + str(nbr)
								not_infected.remove(nbr)
								got_inf.append(nbr)
						index+=1
					if(nodestopsinfet):
						cantinfectmore.append(node)
			infecting_index+=1
		if(len(got_inf)==0):
			breakcount+=1
		else:
			breakcount=0
		if(breakcount==3):
			break
		infected.append(got_inf)
		#print "sleeping.."
		#time.sleep(2)
		currtime+=1

def sirwithstartnodes():
	#for top4, 3, and 2
	top=[2]
	for top_index in top:
		i=0
		for measure in measures:
			print "********** STARTING FOR MEASURE "+measure+" top "+str(top_index)+"**************"
			global infected
			global not_infected
			global consider_weight
			if(consider_weight):
				consider_weight = False
			else:
				consider_weight = True
			reset()
			filename = "multinodes/top"+str(top_index)+"/sir_vals_"+measure+".txt"
			f = open(filename,'w')
			infected = [start_nodes[i][0:top_index]]
			for startnode in start_nodes[i][0:top_index]:
				not_infected.remove(startnode)
				
			if(consider_weight):
				sirhelper(-1)
			else:
				sirhelper(0.1)
			
			total_infected = 0
			for t in infected:
				f.write(str(len(t))+",")
				total_infected+=len(t)
				liststr = str(t)
				liststr = liststr.strip('[]')
				f.write(liststr+"\n")
			f.close()
			i+=1

sirwithstartnodes()