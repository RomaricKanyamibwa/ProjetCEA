# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:20:47 2017

@author: colette
"""

import numpy as np
from matplotlib import pyplot as plt
from mshToPython_triangle import *
from dessine_python import *
from intersection import *
from delet_doublons import *
from barycentre import *  

   
##chargement des donnees et initialisation------------------------------------------------------------------------------------------------------------   
   
(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("Fichier_MSH/m1.msh")
(nodes2, elems2, n_nodes_2, n_elems_2) = mshToPython_triangle("Fichier_MSH/m2.msh")
informations = [nodes1, elems1, nodes2, elems2]

nodes3 = []
elems3 = []
n_elems_3 = 0
nodes3 = []
n_nodes_3 = n_nodes_1 

##code ------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(n_nodes_1): #recopie les nodes de 1, attention ne prend pas en compte les noeuds différent de 2
    nodes3.append(nodes1[i])
for i in range(n_nodes_2): #recopie les nodes de 1, attention ne prend pas en compte les noeuds différent de 2
    nodes2[i][0] = nodes2[i][0] + n_nodes_3
    nodes3.append(nodes2[i])
n_nodes_3 = n_nodes_3 + n_nodes_2

for t1 in range(n_elems_1): #triangle du maillage 1
    for t2 in range(n_elems_2): #triangle du maillage 2
        pt_intersection = []
        nb_pt_inter = 0
        for s1 in range(3): # segments du triangle du maillage 1
            for s2 in range(3):#3): # segments du triangle du maillage 2
                #on cherche le point d'intersection de deux segments l'un d'un triangle t1 et l'autre d'un t2
                R = intersection(t1,t2,s1,s2,informations)
                if(R):
                    print R
                    pt_intersection.append(R)
                    nb_pt_inter = nb_pt_inter + 1
                    print(nb_pt_inter)
        if(nb_pt_inter > 0):
            (xb,yb) = barycentre(pt_intersection,nb_pt_inter)
            n_nodes_3 = n_nodes_3 + 1
            n_bary = n_nodes_3
            nodes3.append([n_nodes_3, xb,yb,0])
            for i in range(2): #trinagle 0, triangle 1
                for j in range(nb_pt_inter):
                    for k in range(j,nb_pt_inter):
                        if(pt_intersection[j][6+i]==pt_intersection[k][6+i] and (pt_intersection[j][0]!=pt_intersection[k][0] or pt_intersection[j][1]!=pt_intersection[k][1])): #un segment du triangle i est coupé par 2 segments de lautre triangle
                            print pt_intersection[j],pt_intersection[k]                            
                            n_nodes_3 = n_nodes_3 + 1
                            nodes3.append([n_nodes_3, pt_intersection[k][0],pt_intersection[k][1],0])                            
                            n_nodes_3 = n_nodes_3 + 1
                            nodes3.append([n_nodes_3, pt_intersection[j][0],pt_intersection[j][1],0])
                            n_elems_3 = n_elems_3 + 1
                            
                            toto1 = n_nodes_3
                            toto2 = n_nodes_3 -1
                            elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])
                            #trouver le sommet commun entre les 2 segments du triangle i+1 (qui coupent deux fois l'un des segments du triangle i)                            
                            if(i==0):
                                seg1 = pt_intersection[j][7] #segment 1 de t2
                                seg2 = pt_intersection[k][7] #segment 2 de t2
                                print seg1,seg2
                                if(seg1==2):
                                    seg1_1 = elems2[t2][3] #somment 1 seg 1
                                    seg1_2 = elems2[t2][1] #sommmet 2 seg 2
                                else:
                                    seg1_1 = elems2[t2][seg1+1] #somment 1 seg 1
                                    seg1_2 = elems2[t2][seg1+2] #sommmet 2 seg 2
                                if(seg2==2):
                                    seg2_1 = elems2[t2][3] #somment 1 seg 1
                                    seg2_2 = elems2[t2][1] #sommmet 2 seg 2
                                else:
                                    seg2_1 = elems2[t2][seg2+1] #somment 1 seg 1
                                    seg2_2 = elems2[t2][seg2+2] #sommmet 2 seg 2
                                print seg1_1,seg1_2,seg2_1,seg2_2
                                if(nodes2[seg1_1-1][1]==nodes2[seg2_1-1][1] and nodes2[seg1_1-1][2]==nodes2[seg2_1-1][2]):
                                    n_sommet = seg1_1
                                    print "seg1_1 seg2_1"
                                    print seg1_1, seg2_1
                                if(nodes2[seg1_1-1][1]==nodes2[seg2_2-1][1] and nodes2[seg1_1-1][2]==nodes2[seg2_2-1][2]):
                                    n_sommet = seg1_1
                                    print "seg1_1 seg2_2"
                                    print seg1_1, seg2_2
                                if(nodes2[seg1_2-1][1]==nodes2[seg2_1-1][1] and nodes2[seg1_2-1][2]==nodes2[seg2_1-1][2]):
                                    n_sommet = seg1_2
                                    print "seg1_2 seg2_1"
                                    print seg1_2, seg2_1
                                if(nodes2[seg1_2-1][1]==nodes2[seg2_2-1][1] and nodes2[seg1_2-1][2]==nodes2[seg2_2-1][2]):
                                    n_sommet = seg1_2
                                    print "seg1_2 seg2_2"
                                    print seg1_2, seg2_2
                                n_elems_3 = n_elems_3 + 1
                                elems3.append([n_elems_3, n_sommet - (i-1)*3, toto1,toto2])
                            if(i==1):
                                seg1 = pt_intersection[j][6] #segment 1 de t2
                                seg2 = pt_intersection[k][6] #segment 2 de t2
                                print seg1,seg2
                                if(seg1==2):
                                    seg1_1 = elems1[t2][3] #somment 1 seg 1
                                    seg1_2 = elems1[t2][1] #sommmet 2 seg 2
                                else:
                                    seg1_1 = elems1[t2][seg1+1] #somment 1 seg 1
                                    seg1_2 = elems1[t2][seg1+2] #sommmet 2 seg 2
                                if(seg2==2):
                                    seg2_1 = elems1[t2][3] #somment 1 seg 1
                                    seg2_2 = elems1[t2][1] #sommmet 2 seg 2
                                else:
                                    seg2_1 = elems1[t2][seg2+1] #somment 1 seg 1
                                    seg2_2 = elems1[t2][seg2+2] #sommmet 2 seg 2
                                print seg1_1,seg1_2,seg2_1,seg2_2
                                if(nodes1[seg1_1-1][1]==nodes1[seg2_1-1][1] and nodes1[seg1_1-1][2]==nodes1[seg2_1-1][2]):
                                    n_sommet = seg1_1
                                    print "seg1_1 seg2_1"
                                    print seg1_1, seg2_1
                                if(nodes1[seg1_1-1][1]==nodes1[seg2_2-1][1] and nodes1[seg1_1-1][2]==nodes1[seg2_2-1][2]):
                                    n_sommet = seg1_1
                                    print "seg1_1 seg2_2"
                                    print seg1_1, seg2_2
                                if(nodes1[seg1_2-1][1]==nodes1[seg2_1-1][1] and nodes1[seg1_2-1][2]==nodes1[seg2_1-1][2]):
                                    n_sommet = seg1_2
                                    print "seg1_2 seg2_1"
                                    print seg1_2, seg2_1
                                if(nodes1[seg1_2-1][1]==nodes1[seg2_2-1][1] and nodes1[seg1_2-1][2]==nodes1[seg2_2-1][2]):
                                    n_sommet = seg1_2
                                    print "seg1_2 seg2_2"
                                    print seg1_2, seg2_2
                                n_elems_3 = n_elems_3 + 1
                                elems3.append([n_elems_3, n_sommet - (i-1)*3, toto1,toto2])
                                
delet_doublon(nodes3,elems3,informations)                          

dessine_python(nodes3,elems3)