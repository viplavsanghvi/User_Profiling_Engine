import pandas as pd
import numpy as np

f_handle=open("./data/yoochoose-solution.dat")
i=0
f = open('correct_solution', 'w')
for row in f_handle:
	mylist=row.split(';')
	session=mylist[0]
	items=mylist[1].split(',')
	for j in range(len(items)):
		items[j]=int(items[j])
		line=session + "," + str(items[j]) + "," + '1' +"\n"
		f.write(line)
f.close()
