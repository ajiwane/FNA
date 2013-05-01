import math
import random 

filename = "randoms2.txt"
f = open(filename,'w')
for i in range(1000000):
	f.write(str(round(random.random(),4))+"\n")
f.close()


filename = "randoms3.txt"
f = open(filename,'w')
for i in range(1000000):
	f.write(str(round(random.random(),4))+"\n")
f.close()