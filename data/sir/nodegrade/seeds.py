# Normal SI Model - BoxPlot - T vs P
import os
import numpy as nm
centrality = ["eigen", "page", "degree"]
probab = ['0.1','w']
for c in centrality:
	# Initializing measure list
	measure = []
	for i in range(len(probab)):
		measure.append([])
		
	for files in os.listdir("."):
		if files.endswith(".txt"):
			file = files.strip(".txt")
			file = files.split("_")
			# Check for Centrality and do only for "1 infected node"
			if file[2] == c and file[4] == "random1.txt":
				if file[1] in probab:
					# print files
					i = probab.index(file[1])
					timesteps = 0
					f = open(files,"r")
					cumfreq = 0
					for line in f:
						if line.strip():
							data = line.split(",")
							if int(data[0]) == 0:
								break
							cumfreq += int(data[0])
							timesteps += 1
					f.close()
					ti = []
					ti.append(file[3])
					ti.append(cumfreq)
					ti.append(timesteps)
					measure[i].append(ti)
	print measure
	# filename = "seed_"+c+".csv"
	# g = open(filename,"w")
	# x = ','.join(probab)
	# g.write(x+"\n")
	
	# for m in range(len(measure[0])):
		# for n in range(len(measure)):
			# g.write(str(measure[n][m])+",")
		# g.write("\n")
		
	# for m in measure:
		# for n in m:
			# x = str(n)
			# x = x.strip("[]")
			# g.write(x+"\n")
	# g.write("\n")
	# for m in measure:
		# v = nm.std(m)
		# g.write(str(v)+",")
	# g.write("\n")	
	# for m in measure:
		# v = nm.std(m)
		# g.write(str(v)+",")
	# g.write("\n")				
			
