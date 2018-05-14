# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:01:39 2018
fonction qui prend en arguement un fichier .msh et renvoie en python un tableau de noeud, un d'élément, et les tailles de ces matrices
"""

import numpy as np

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

    elems = []

    for line in f1:
        ligne = line.split(' ')
        if(ligne[0]!='$EndElements\r\n' and ligne[0]!='$EndElements\n'):
            ligne = list(map(int, ligne))
            if(ligne[1]==2):
                del ligne[1]
                for i in range(ligne[1]+1):
                    del ligne[1]
                elems.append(ligne)
        
    f1.close()
    n_elems = len(elems)
    
    for i in range(n_elems):
        elems[i][0] = i+1
    return (nodes, elems, n_nodes, n_elems)    