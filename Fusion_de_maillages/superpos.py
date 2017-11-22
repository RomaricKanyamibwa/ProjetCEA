# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:20:47 2017

@author: colette
"""

import numpy as np
from __futur__ import division

def extrait_info(nom_fichier):
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
        elem.append(ligne)
        
    f1.close()
    return (nodes, elem, n_nodes, n_elems)
    
def line(p1,p2):
    A = (p1[1]-p2[1])
    B = (p2[0]-p1[0])
    C = (p1[0]*p2[1]-p2[0]*p1[1])
    return A,B,-C
    
def intersection(L1,L2):
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
    
    
    
(nodes1, elem1, n_nodes_1, n_elems_1) = extrait_info("maillage1.msh")
(nodes2, elem2, n_nodes_2, n_elems_2) = extrait_info("maillage2.msh")



for i in range(n_nodes_1):
    for j in range(i+1,n_nodes_2):
        inter = sorted(list(set([nodes1[i][-1],nodes1[i][-2],nodes1[i][-3]]) & set([nodes1[j][-1],nodes1[j][-2],nodes1[j][-3]])))
        if(len(inter)==2): #nb de pt commun
            troisiem1 =  