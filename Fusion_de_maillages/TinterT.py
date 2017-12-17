""" Programm for playing the game skyline """
#from random import randrange

import numpy as np

elem1 = np.array([
			[1,4,7,3],
			[2,4,5,3],
			[3,3,8,6],
			[4,4,8,1]])

elem2 = np.array([
			[1,2,7,3],
			[2,4,5,6],
			[3,3,8,9],
			[4,4,8,9]])

def TinterT(msh1,msh2):
	len1 = len2 = 0
	for sub_list in msh1 : len1 += 1
#	print("1- number of items: %d" % len1)
	for sub_list in msh2 : len2 += 1
#	print("2- number of items: %d" % len2)
	num_T = []
	new_msh1 = msh1.flatten()
	for k,v in enumerate(new_msh1):
		if (k%len1) == 0:
			num_T.append(v)
#	print(num_T)
#	print(new_msh1)
	new_msh2 = msh2.flatten()
	for k,v in enumerate(new_msh2):
		if (k%len2) == 0:
			num_T.append(v)
	print(num_T)
#	print(new_msh2)
	i = 0
	neighB = []
	fin = True
	while fin:
		print("+ %d:" % num_T[i])
		j = len1
		while j > i and j < len1+len2:
			print("%d" % num_T[j], end=' ')
			# S'il y a intersection entre le triangle 1 du mesh1 et les triangles 1,2,3,4 du mesh2:
			if intersect():
				# On ajoute les triangles voisins des triangles 1,2,3,4 du mesh2 à neighB
				neighB.append(neighbors())
				# On parcourt la liste neighB
			while v in neighB:
				# Si un des triangles voisins des triangles 1,2,3,4 du mesh2 ne s'intersecte pas avec le triangle 1 du mesh1:
				if not intersect():
					# On retire ce triangle de la liste neighB
					del v
			j += 1
			if j == len1+len2:
				j = i
		print()
		i += 1
		if i >= len1:
			fin = False


# Si le triangle 1 du mesh1 s'intersecte (methode intersect() ?? pas moyen de tester) avec les triangles 1,2,3,4 du mesh2 Alors 
# on check si les triangles voisins (methode neighbors()) des triangles 1,2,3,4 du mesh2 s'intersectent aussi avec le triangle 1 du mesh1

TinterT(elem1,elem2)
TinterT(elem2,elem1)
