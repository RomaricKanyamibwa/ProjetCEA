# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:03:18 2018

@author: colette
"""

from mshToPython_triangle import *
from neighbors import *

(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("Fichier_MSH/maillage1.msh")

def old_formalisation_to_new(node, elem):
    n_node = len(node)
    n_elem = len(elem)
        
    new_node = [[0,0,0] for i in range(n_node)]
    new_elem = [[0,0,0] for i in range(n_elem)]    
    
    for i in range(n_node):
        for j in range(3):
            new_node[i][j] = node[i][j+1]
    for i in range(n_elem):
        for j in range(3):
            new_elem[i][j] = elem[i][j+1] - 1
    return(new_node, new_elem)
    
def new_formalisation_to_old(node, elem):
    n_node = len(node)
    n_elem = len(elem)
        
    new_node = [[0,0,0,0] for i in range(n_node)]
    new_elem = [[0,0,0,0] for i in range(n_elem)]    
    
    for i in range(n_node):
        new_node[i][0] = i + 1
        for j in range(3):
            new_node[i][j+1] = node[i][j]
    for i in range(n_elem):
        new_elem[i][0] = i + 1 
        for j in range(3):
            new_elem[i][j+1] = elem[i][j] + 1
    return(new_node, new_elem)
    
def old_formalisation_to_new_arrete(arrete):
    n_arrete = len(arrete)
    
    new_arrete = [[] for i in range(n_arrete)]
    
    i=0
    for k in arrete.keys():
        if(len(arrete[k])==1):
            new_arrete[i].append((k[0]-1,k[1]-1))
            new_arrete[i].append([arrete[k][0] -1])
            i = i+1
        elif(len(arrete[k])==2):
            new_arrete[i].append((k[0]-1,k[1]-1))
            new_arrete[i].append([arrete[k][0] -1,arrete[k][1] -1])
            i = i+1

    return(new_arrete)
    


(maxi,arrete) = list_neighbors(elems1)
(node, elem) = old_formalisation_to_new(nodes1, elems1)  

print ""


new_arrete = old_formalisation_to_new_arrete(arrete)
print "new arrete"
print new_arrete
print "arrete"
print arrete



def remplissage_A1(node, elem, arrete): # il faut faire la tranposer
    nb_arrete = len(arrete)
    nb_sommet = len(node)
    nb_triangle = len(elem)
    
    A1 = [[0 for i in range(nb_sommet)] for i in range(nb_arrete)] #arrete sommet
    print A1
    
    for i in range(nb_arrete):
        ind1 = arrete[i][0][0]
        ind2 = arrete[i][0][1]
        A1[i][ind1] = 1
        A1[i][ind2] = -1
    return A1
    
def remplissage_A2(node, elem, arrete): 
    nb_arrete = len(arrete)
    nb_sommet = len(node)
    nb_triangle = len(elem)
    
    A2 = [[0 for i in range(nb_triangle)] for i in range(nb_arrete)] #arrete sommet
    
    for i in range(nb_arrete):
        sommet1 = arrete[i][0][0]
        sommet2 = arrete[i][0][1]
        
        tri1 = arrete[i][1][0]
        print "tri1"
        print tri1
        j = 0
        while(elem[tri1][j]!=sommet1):
            j=j+1
        if(elem[tri1][(j+1)%3]==sommet2):
            A2[i][tri1]=1
        else:
            A2[i][tri1]=-1
                
        if(len(arrete[i][1])==2):
            tri2 = arrete[i][1][1]
            j = 0
            while(elem[tri2][j]!=sommet1):
                j=j+1
            if(elem[tri2][(j+1)%3]==sommet2):
                A2[i][tri2]=1
            else:
                A2[i][tri2]=-1

    return A2


print remplissage_A1(node, elem, new_arrete)
print remplissage_A2(node, elem, new_arrete)