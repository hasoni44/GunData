import pandas
import numpy
import csv
import matplotlib.pyplot
from datetime import datetime


#-------------------------------------------------------------------------------

#read the file and put it in a 2d list
gundata = open("gun-data.csv",'r').read().splitlines()
gundata = [i.split(",") for i in gundata]

#only use the data from 2017
gundata = gundata[1:496]

#to save all of the states and their respective numbers
states = []

#go through each state
for i in range(0,55):
	
	#save what state your working on
	currentState = gundata[i][1]
	#save how many permits the respective state has
	currentPermits = 0
	#used to add to larger 2d list
	combo = []
	
	#go through each of the states months that are in 2017
	for j in range(0,9):
		#continously add to the permits 
		currentPermits += int(gundata[i+j][2])
	
	#add the state and permit value 
	combo.append(currentState)
	combo.append(currentPermits)
	
	#add these combined values to a large list
	states.append(combo)

#write this large list in to a csv file as your final answer
with open("filteredgundata.csv","w+") as f:
	writer = csv.writer(f,delimiter=",")
	writer.writerows(states)
		
		



