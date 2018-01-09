# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:20:47 2017

@author: colette
"""

import numpy as np
from matplotlib import pyplot as plt


def mshToPython(nom_fichier):
    f1 = open(nom_fichier)

    li = f1.readline().split() 

    while(li[0]!="$Nodes"):  #lire la ligne suivante tant que pas arriver à $Nodes
        li = f1.readline().split() # '$Nodes\n'

    n_nodes = int(f1.readline())

    nodes = np.fromfile(f1,count=n_nodes*4, sep=" ").reshape((n_nodes,4)) #tableau des noeuds

    f1.readline() # '$EndNodes\n'
    f1.readline() # '$Elements\n'
    n_elems = int(f1.readline()) # '2\n'

    elem = []

    for line in f1:
        ligne = line.split(' ')
        if(ligne[0]!='$EndElements\r\n'):
            ligne = map(int, ligne)
            elem.append(ligne)
        
    f1.close()
    return (nodes, elem, n_nodes, n_elems)
    
    
    
def mshToPython_triangle(nom_fichier):
    f1 = open(nom_fichier)

    li = f1.readline().split() 

    while(li[0]!="$Nodes"):  #lire la ligne suivante tant que pas arriver à $Nodes
        li = f1.readline().split() # '$Nodes\n'

    n_nodes = int(f1.readline())

    nodes = np.fromfile(f1,count=n_nodes*4, sep=" ").reshape((n_nodes,4)) #tableau des noeuds

    f1.readline() # '$EndNodes\n'
    f1.readline() # '$Elements\n'
    n_elems = int(f1.readline()) # '2\n'

    elem = []

    for line in f1:
        print(line)
		ligne = line.split(' ')
        if(ligne[0]!='$EndElements\r\n'):
            ligne = map(int, ligne)
            if(ligne[1]==2):
                del ligne[1]
                for i in range(ligne[1]+1):
                    del ligne[1]
                elem.append(ligne)
        
    f1.close()
    n_elems = len(elem)
    return (nodes, elem, n_nodes, n_elems)    
    
def line(p1,p2):
    A = (p1[1]-p2[1])
    B = (p2[0]-p1[0])
    C = (p1[0]*p2[1]-p2[0]*p1[1])
    return A,B,-C
    
def intersection(L1,L2,p11,p12,p21,p22):
    if(L1[1]==0 and L2[1]==0):
        #print "colinéaire"
        #print "infini"
        return False
    if(L1[0]/float(L1[1])==L2[0]/float(L2[1])): #colinéaire
        #print "colinéaire"
        return False
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        #segment
        if(x<=min(p11[0],p12[0]) or x>=max(p11[0],p12[0]) or y<=min(p11[1],p12[1]) or y>=max(p11[1],p12[1]) or x<=min(p21[0],p22[0]) or x>=max(p21[0],p22[0]) or y<=min(p21[1],p22[1]) or y>=max(p21[1],p22[1]) ):
            #print "seg"
            return False
        return x,y,p11[2],p12[2],p21[2],p22[2]
    else:
        return False
        #print "ne se croise pas"




"""        
def pythonToMsh(nodes, elem):
    n_nodes = len(nodes)
    n_elems = len(elem)
"""    
    
    
(nodes1, elem1, n_nodes_1, n_elems_1) = mshToPython_triangle("maillage1.msh")
(nodes2, elem2, n_nodes_2, n_elems_2) = mshToPython_triangle("maillage2.msh")


nodes3 = []
elem3 = []
n_elems_3 = 0
nodes3 = []
n_nodes_3 = n_nodes_1

for i in range(n_nodes_1):
    nodes3.append(nodes1[i])

for t1 in range(n_elems_1): #triangle du maillage 1
    for t2 in range(n_elems_2): #triangle du maillage 2
        pt_intersection = []
        nb_pt_inter = 0
        for s1 in range(3): # segments du triangle du maillage 1
            for s2 in range(3): # segments du triangle du maillage 2
                #on cherche le point d'intersection de deux segments l'un d'un triangle t1 et l'autre d'un t2
                p11 = [nodes1[elem1[t1][s1+1]-1][1],nodes1[elem1[t1][s1+1]-1][2],elem1[t1][s1+1]]
                p12 = [nodes1[elem1[t1][(s1+1)%3+1]-1][1],nodes1[elem1[t1][(s1+1)%3+1]-1][2],elem1[t1][(s1+1)%3+1]]
                p21 = [nodes2[elem2[t2][s2+1]-1][1],nodes2[elem2[t2][s2+1]-1][2],elem2[t2][s2+1]]
                p22 = [nodes2[elem2[t2][(s2+1)%3+1]-1][1],nodes2[elem2[t2][(s2+1)%3+1]-1][2],elem2[t2][(s2+1)%3+1]]
                L1 = line(p11,p12)
                L2 = line(p21,p22)              
                R = intersection(L1,L2,p11,p12,p21,p22)
                if(R):
                    pt_intersection.append(R)
                    nb_pt_inter = nb_pt_inter + 1
                    n_nodes_3 = n_nodes_3 + 1
                    nodes3.append([n_nodes_3, R[0],R[1],0])
                    elem3.append([n_elems_3, n_nodes_3, R[2],R[4]])
                    n_elems_3 = n_elems_3 + 1
                    elem3.append([n_elems_3, n_nodes_3, R[2],R[5]])
                    n_elems_3 = n_elems_3 + 1
                    elem3.append([n_elems_3, n_nodes_3, R[3],R[4]])
                    n_elems_3 = n_elems_3 + 1
                    elem3.append([n_elems_3, n_nodes_3, R[3],R[5]])
                    n_elems_3 = n_elems_3 + 1

  
        

for i in range(n_elems_3):    
	p1 = elem3[i][1]
	p2 = elem3[i][2]
	p3 = elem3[i][3]
	x = [nodes3[p1-1][1],nodes3[p2-1][1],nodes3[p3-1][1],nodes3[p1-1][1]]
	y = [nodes3[p1-1][2],nodes3[p2-1][2],nodes3[p3-1][2],nodes3[p1-1][2]]
	plt.plot(x, y)
plt.axis('equal')   # ajout
                
def dessine_python(node,elem):
	for i in range(len(elem)):
		p1 = int(elem[i][1])
		p2 = int(elem[i][2])
		p3 = int(elem[i][3])
		x = [node[p1-1][1],node[p2-1][1],node[p3-1][1],node[p1-1][1]]
		y = [node[p1-1][2],node[p2-1][2],node[p3-1][2],node[p1-1][2]]
		plt.plot(x, y)
	plt.axis('equal')
#-----------------------------------------------------------------------

for x in elem1[1:]:
	t = (elem1[x][1],elem1[x][2]).sort()
	s = (elem1[x][2],elem1[x][3]).sort()
	r = (elem1[x][1],elem1[x][3]).sort()
	d1 = dict(t.append(x),s.append(x),r.append(x))
print(d1.items)

for x in elem2[1:]:
	t = (elem2[x][1],elem2[x][2]).sort()
	s = (elem2[x][2],elem2[x][3]).sort()
	r = (elem2[x][1],elem2[x][3]).sort()
	d2 = dict(t.append(x),s.append(x),r.append(x))
print(d2.items)

for x in elem3[1:]:
	t = (elem3[x][1],elem3[x][2]).sort()
	s = (elem3[x][2],elem3[x][3]).sort()
	r = (elem3[x][1],elem3[x][3]).sort()
	d = dict(t.append(x),s.append(x),r.append(x))
print(d.items)

	
n1 = input("De quel triangle souhaitez-vous connaître ses voisins ? Je veux connaître ceux du triangle numéro :")

def neighbours(elem,dx):
#	if n1 in d1.values :
	a = numpy.zeros(shape=(len(elem)+1,len(elem)+1)
	for i in a:
		a[i,1] = i
	for i in dx.values	
		if j != i
			a[i,j]=j 
	return(a)

a1 = neighbours(elem1,d1)
a2 = neighbours(elem2,d2)
a3 = neighbours(elem3,d)

#	for v in di if di :
#		neighboursOfneighbour(v,d)

def neighboursOfneighbour(a1,a2)
	b = numpy.zeros(shape=(len(a1)+len(a2),len(a1)+len(a2)))
	if i in a1[i,0]:
		for t in a1[i,:]
			if intersection(i,t) == True
				b[i] = append(t)
				







#-----------------------------------------------------------------------

	

