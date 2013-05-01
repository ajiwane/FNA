probs = [0.3,0.2,0.1,0.05] 
start_nodes_withoutwt = [3381,1868,100]
start_nodes_withwt = [1641,2160,100]
consider_weight = False
randomfiles =["random1","random2","random3"]
for ran in randomfiles:
	excelfile = open(ran+"_excel.csv","w")
	for sn in start_nodes_withoutwt:
		freqline=str(sn)+","
		cumfreqline=str(sn)+","
		for prob in probs:
			filename = ran+"/si_vals_"+str(prob)+"_"+str(sn)+".txt"
			f = open(filename,'r')
			freqline+=str(prob)+",frequency,"
			cumfreqline+=str(prob)+",cummfreq,"
			total_infected = 0
			#timestep=1
			line = f.readline()
			while line:
				line = line.strip()
				line = line.split(",")
				infected = int(line[0])
				total_infected+=infected
				freqline+=str(infected)+","
				cumfreqline+=str(total_infected)+","
				#timestep+=1
				line = f.readline()
			f.close()
			freqline+="\n"
			cumfreqline+="\n"
			excelfile.write(freqline)
			excelfile.write(cumfreqline)

	for sn in start_nodes_withwt:
		filename = ran+"/si_vals_withweighted_"+str(sn)+".txt"
		f = open(filename,'r')
		freqline=str(sn)+",weight,frequency,"
		cumfreqline=str(sn)+",weight,cummfreq,"
		total_infected = 0
		line = f.readline()
		while line:
			line = line.strip()
			line = line.split(",")
			infected = int(line[0])
			total_infected+=infected
			freqline+=str(infected)+","
			cumfreqline+=str(total_infected)+","
			#timestep+=1
			line = f.readline()
		f.close()
		freqline+="\n"
		cumfreqline+="\n"
		excelfile.write(freqline)
		excelfile.write(cumfreqline)		
	excelfile.close()

