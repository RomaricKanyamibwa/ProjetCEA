# -*- coding: utf-8 -*-
"""Voisin des triangles """
#from random import randrange

#import numpy as np
#from tinter import mshToPython_triangle

elem3 = [[1,2,7,3],
	[2,4,5,6],
	[3,3,8,9],
	[4,4,8,9],
    [5,7,5,2],
    [6,7,4,2]]
    

#(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("maillage1.msh")
#(nodes2, elems2, n_nodes_2, n_elems_2) = mshToPython_triangle("maillage2.msh")
elems1=[[1, 1, 5, 9], [2, 1, 8, 9], [10, 5, 6, 9], [4, 2, 5, 6], [5, 3, 6, 9], [6, 3, 7, 9], [7, 7, 8, 9], [8, 4, 7, 8]]

def list_neighbors(triangles):
    """Fonction de  construction de dictionaire de voisin
    Entree:
    -triangles: une liste de n triangles avec leurs sommets
    Sortie:
    -num_triangles
    -d:dictionaire de voisins
    """
    d = dict()
    maximum=0
    for x in triangles:
        maximum=max(x[0],maximum)
        x[1:]=sorted(x[1:],key=int)
        #print(x)
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
    print(maximum)
    #num_triangles=len(triangles)
    return maximum,d
print(elems1)
n,d=list_neighbors(elems1)	
print(d)
#n1 = input("De quel triangle souhaitez-vous connaître ses voisins ? Je veux connaître ceux du triangle numéro :")

def neighbours(elem):
    """Fonction qui retourne la liste des voisins de triangles
    Arguments:
    -elem: liste des triangles
    -dx: dictionaire contenant les voisins (on utilise la fonction list_neighbors)
    Sortie;
    -a:liste des voisind de triangles
    
    """
#	cette fonction est pour le maillage conforme
    n,dx=list_neighbors(elem)
    a = [[]]*(n+1)
#    print("len",len(elem))
#    for i in range(1,len(elem)) :
#        a[i] = [i]
    for x in dx.values():
        #print(x)
        if(len(x)==2):
            #print((x[0]))
            a[x[0]]=a[x[0]]+[x[1]]
#            print(x[1])
            a[x[1]]=a[x[1]]+[x[0]]
#            print(a)
        elif(len(x)==3):
            a[x[0]]=a[x[0]]+[x[1],x[2]]
            a[x[1]]=a[x[1]]+[x[0],x[2]]
            a[x[2]]=a[x[2]]+[x[1],x[0]]
#        if i in j:
#            tmp=j
#            tmp.remove(i)
#            a[i]+=tmp
    print(a)
    return(a)

a3 = neighbours(elems1)
