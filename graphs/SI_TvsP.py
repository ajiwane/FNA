# Normal SI Model - BoxPlot - T vs P
import os
import numpy as nm
centrality = ["eigen", "page", "degree"]
probab = ['0.3','0.2','0.1','0.05',"w"]
for c in centrality:
	# Initializing measure list
	measure = []
	for i in range(5):
		measure.append([])
		
	for files in os.listdir("."):
		if files.endswith(".txt"):
			file = files.strip(".txt")
			file = files.split("_")
			# Check for Centrality and do only for "1 infected node"
			if file[2] == c and file[3] == "1":
				if file[1] in probab:
					# print file
					i = probab.index(file[1])
					timesteps = 0
					f = open(files,"r")
					for line in f:
						if line.strip():
							timesteps += 1
					f.close()
					measure[i].append(timesteps)
	# print measure
	filename = "TvsP_"+c+".csv"
	g = open(filename,"w")
	x = ','.join(probab)
	g.write(x+"\n")
	
	# for m in range(len(measure[0])):
		# for n in range(len(measure)):
			# g.write(str(measure[n][m])+",")
		# g.write("\n")
		
	for m in measure:
		v = nm.mean(m) - nm.std(m)
		g.write(str(v)+",")
	g.write("\n")
	for m in measure:
		v = nm.std(m)
		g.write(str(v)+",")
	g.write("\n")	
	for m in measure:
		v = nm.std(m)
		g.write(str(v)+",")
	g.write("\n")				
			
