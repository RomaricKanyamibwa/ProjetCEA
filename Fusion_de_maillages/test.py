""" Programm for playing the game skyline """
#from random import randrange

import numpy as np

elem3 = [[1,2,7,3],
	[2,4,5,6],
	[3,3,8,9],
	[4,4,8,9]]
d = dict()

for x in elem3[1:]:
	x[1:].sort()
	t = (x[1],x[2])
	s = (x[2],x[3])
	r = (x[1],x[3])
	if t not in d.keys() :
		d[t]=[]
	if s not in d.keys() :
		d[s]=[]
	if r not in d.keys() :
		d[r]=[]	
	d[t].append(x[0]) 
	d[s].append(x[0]) 
	d[r].append(x[0]) 
print(d)

	
#n1 = input("De quel triangle souhaitez-vous connaître ses voisins ? Je veux connaître ceux du triangle numéro :")

def neighbours(elem,dx):
#	if n1 in d1.values :
	a = [[]]*len(elem)
	for i in range(1,len(elem)) :
		a[i] = [i]
	for j in dx.values():	
		print(j)
		if j != i:
			a[i].append(j) 
	print(a)
	return(a)

a3 = neighbours(elem3,d)
