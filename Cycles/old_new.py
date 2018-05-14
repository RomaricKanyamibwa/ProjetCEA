# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:03:18 2018
@author: colette
"""

from mshToPython_triangle import *
from neighbors import *
from numpy.linalg import matrix_rank
from homology_calc import *
from n_holes import *

##########################################   FONCTIONS   ########################################

def old_formalisation_to_new(node, elem):
    """
    permet de tranformer les tableaux node et elem de la formalisation de
    la première partie du projet à celle de la deuxième
    """
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
    #print("eee")
    for k in arrete.keys():
        #print("lenarrete")
        #print(len(arrete[k]))
        if(len(arrete[k])==1):
            new_arrete[i].append((k[0]-1,k[1]-1))
            new_arrete[i].append([arrete[k][0] -1])
            i = i+1
        elif(len(arrete[k])==2):
            new_arrete[i].append((k[0]-1,k[1]-1))
            new_arrete[i].append([arrete[k][0] -1,arrete[k][1] -1])
            i = i+1

    return(new_arrete)
    
def remplissage_A1(node, elem, arrete): # il faut faire la transposer
    nb_arrete = len(arrete)
    nb_sommet = len(node)
    nb_triangle = len(elem)
    
    A1 = [[0 for i in range(nb_sommet)] for i in range(nb_arrete)] #arrete sommet
    #print A1
    
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
        #print arrete[i]
        sommet1 = arrete[i][0][0]
        sommet2 = arrete[i][0][1]
        #print sommet1
        
        tri1 = arrete[i][1][0]
        #print "tri1"
        #print tri1
        j = 0
        while(elem[tri1][j]!=sommet1):
            #print elem[tri1][j]
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
    
##########################################   MAIN   ###########################################
    
    
#(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("ex.msh")

#changement de elems1 parce que probleme, chaque triangle est répété deux fois
#elems1 = elems1[::2]
#for i in range(len(elems1)):
    #elems1[i][0] = i+1

#construit un dictionnaire d'arretes   
(nodes1,elems1) = nb_holes(3)
#draw_cycle([], nodes1, elems1, [])
(nodes1,elems1) = new_formalisation_to_old(nodes1, elems1)

#construit un dictionnaire d'arretes   
(maxi,arrete) = list_neighbors(elems1)

#change en nouvelle formalisation
(node, elem) = old_formalisation_to_new(nodes1, elems1)  
new_arrete = old_formalisation_to_new_arrete(arrete) #changement de 
#draw_cycle([], node, elem, [])

#creation des matrices de cohomologie
A1 = remplissage_A1(node, elem, new_arrete)
A2 = remplissage_A2(node, elem, new_arrete)




dim_Im_A2 = matrix_rank(A2)
n = np.shape(A1)[0]             #size(A1)/len(A1)
dim_Ker_A1 = n - matrix_rank(A1) #rang theorem
print("nb Betty")
print(dim_Ker_A1- dim_Im_A2)

Betti_number_SNF,KerM_SNF= Select_Kernel_Method(SparseMatrix(A1).T,SparseMatrix(A2),method=2,display=false)
print("KerM_SNF:")
pprint(KerM_SNF)


'''
#arrete = [[(sommet1,sommet2),[triangle(s)]],[...],[...]]
vect1 = [0 ,-15718, -136 , 0, 6160 ,0  , 4183 ,-1441 ,  0  ,15718,-24973,-24973, 0 ,1573 ,20790 ,-9046 ,-9255 ,-6024 ,20790 ,-9255,9046 ,11608,136 , 136  ,-9694 ,24973 ,1705 ,7341,-4183 ,9694 ,-1573,
-15718,9255,-1705,11608,-11608,9182 , 3146 ,20790 , 9182 , 9255 ,9255,-9182,11608 , 3014 ,-9255 ,-6024 ,-11608,20790 ,-2353 ,1441, 1441 ,9255,24973,-20790,-1705,-7341 ,3146 , 6160, 6024 ,-9046,
11608,-3014 ,-7341 ,-20790, 0  ,3014 , 0   ,1705 , 9255,-20790,0 , -136 ,-3146 ,-3146 , 9694 ,2353 ,-9255 , 6160 ,2353 ,-9182 ,-11608,-9694,15718 ,-3014 ,-9255 ,-11608, 9046 , 1441 ,
-9255 , 6160,-9255 ,20790 , 6024 , 2353 ,7341]
vect2 = [-234022,-28094115, 99469, -335423,10956662, -355789,8088287 ,-2660925,355789 ,28094115 ,-44538879,-44538879,582199,2752191 ,36792499 ,
-16073733,-16381552,-11016967,37374698 ,-16046129,16048613 ,20376653 ,-99469 ,
582405  ,-17346246,44140244 ,2843457 ,12862735 ,-6765546 ,17077148 ,-2833532 ,
-27720503,16381552 ,-3210998 ,20732442 ,-20487566,15949144 , 5504382 ,36792499, 
16656138 ,16482953 ,16818376 ,-16656138,20843355 , 5413116 ,-16818376,-10374257,-20732442 ,
37032791 ,-4483511 ,2456066 ,2456066 ,16046129 ,44140244 ,-36450592,-3210998 ,
-13205156,5667064 ,10956662 ,10374257 ,-16073733,20487566 ,-5413116 ,-13205156,
-36450592, 335423  ,5289598 , -234022 , 2843457 ,16248931 ,-37032791,582199  ,
-582405 ,-5667064 ,-5504382 ,17077148 , 3871992 ,-16615574,10917498 ,-4483511 ,
-15949144,-20376653,-17346246,27720503 ,-5289598 ,-16615574,-20843355,16048613 ,
2660925 ,-16482953,10917498 ,-16248931,37374698 ,11016967 ,3871992 ,12862735 ]
for i in range(len(vect1)):
    vect1[i]=vect1[i]%3;
for i in range(len(vect2)):
    vect2[i]=vect2[i]%2;
for i in range(len(vect2)):
    vect2[i]=vect2[i]%3;
for i in range(len(vect2)):
    vect2[i]=vect2[i]%4;
#vect2 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1,
#0, 1, 1, 0, 0, 0, 0, 0, 0 , 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]
#vect3 = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,0,0,0, 1,
#0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1]
draw_cycle(vect2, node, elem, new_arrete)
'''