# Normal SI Model - BoxPlot - T vs P
import os
import numpy as nm
centrality = ["eigen", "page", "degree"]
probab = ['0.3','0.2','0.1','0.05','w']
time = ['1','2','3','4','5']
for t in time:
	for c in centrality:
		measure = []
		# Initializing measure list
		# for i in range(len(probab)):
			# measure.append([])
		for p in probab:
			j = probab.index(p)
			ti = []
			for files in os.listdir("."):
				if files.endswith(".txt"):
					file = files.strip(".txt")
					file = files.split("_")
					# Check for Centrality and do only for "1 infected node"
					if file[2] == c and file[1] == p and file[3] == t:
						count = 0
						print files
						f = open(files,"r")
						for line in f:
							if line.strip():
								data = line.split(",")
								# if int(data[0]) == 0:
									# break
								# print count, len(ti)
								if count < len(ti):
									# print ti[count]
									ti[count].append(int(data[0]))
								else:
									ti.append([int(data[0])])
							count += 1
						# print ti
						f.close()
			ti = [(sum(n)/5.0) for n in ti]
			# print len(ti)
			measure.append(ti)
		print measure
		# print measure
		filename = "Freq_"+c+"_"+t+".csv"
		g = open(filename,"w")
		
		x = ','.join(probab)
		g.write(x+"\n")
		
		# for m in measure:
			# x = str(m)
			# x = x.strip("[]")
			# g.write(probab[measure.index(m)]+","+x+"\n")
		
		# Transposed Matrix - Ready to build plot
		max = 0
		for m in measure:
			if len(m) > max:
				max = len(m)
				
		for m in range(max):
			for n in range(len(measure)):
				print n,m,len(measure[n])
				if (m < len(measure[n])):
					print n,m,len(measure[n])
					g.write(str(measure[n][m])+",")
				else:
					g.write(",")
			g.write("\n")
		
		# x = ','.join(m)	
			
		# for m in measure:
			# v = nm.mean(m) - nm.std(m)
			# g.write(str(v)+",")
		# g.write("\n")
		# for m in measure:
			# v = nm.std(m)
			# g.write(str(v)+",")
		# g.write("\n")	
		# for m in measure:
			# v = nm.std(m)
			# g.write(str(v)+",")
		# g.write("\n")				
					
