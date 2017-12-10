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

    elems = []

    for line in f1:
        ligne = line.split(' ')
        if(ligne[0]!='$EndElements\r\n'):
            ligne = map(int, ligne)
            elems.append(ligne)
        
    f1.close()
    return (nodes, elems, n_nodes, n_elems)
    
    
    
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
            ligne = map(int, ligne)
            if(ligne[1]==2):
                del ligne[1]
                for i in range(ligne[1]+1):
                    del ligne[1]
                elems.append(ligne)
        
    f1.close()
    n_elems = len(elems)
    return (nodes, elems, n_nodes, n_elems)    
    
def line(p1,p2):
    A = (p1[1]-p2[1])
    B = (p2[0]-p1[0])
    C = (p1[0]*p2[1]-p2[0]*p1[1])
    return A,B,-C
    
def intersect(L1,L2,p11,p12,p21,p22,s1,s2):
    #retourne les coordonnés des points d'intersection et les points des segments qui s'intersectent
    if(L1[1]==0 and L2[1]==0):
        #print "colinéaire"
        print "infini"
        return False
    if(L1[0]/float(L1[1])==L2[0]/float(L2[1])): #colinéaire
        print "colinéaire"
        return False
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        #segment
        if(x<min(p11[0],p12[0],p21[0],p22[0]) or x>max(p11[0],p12[0],p21[0],p22[0]) or y<min(p11[1],p12[1],p21[1],p22[1]) or y>max(p11[1],p12[1],p21[1],p22[1])):         
            print "seg"
            return False
        return x,y,p11[2],p12[2],p21[2],p22[2],s1,s2
    else:
        print "ne se croise pas"        
        return False
        
        
def intersection(t1,t2,s1,s2):
   p11 = [nodes1[elems1[t1][s1+1]-1][1],nodes1[elems1[t1][s1+1]-1][2],elems1[t1][s1+1]] #coordonées du point et numéro du point
   p12 = [nodes1[elems1[t1][(s1+1)%3+1]-1][1],nodes1[elems1[t1][(s1+1)%3+1]-1][2],elems1[t1][(s1+1)%3+1]]
   p21 = [nodes2[elems2[t2][s2+1]-1][1],nodes2[elems2[t2][s2+1]-1][2],elems2[t2][s2+1]]
   p22 = [nodes2[elems2[t2][(s2+1)%3+1]-1][1],nodes2[elems2[t2][(s2+1)%3+1]-1][2],elems2[t2][(s2+1)%3+1]]
   L1 = line(p11,p12)
   L2 = line(p21,p22)    
   R = intersect(L1,L2,p11,p12,p21,p22,s1,s2)
   return R

def dessine_python(node,elem):
    for i in range(len(elem)):    
        p1 = int(elem[i][1])
        p2 = int(elem[i][2])
        p3 = int(elem[i][3])
        x = [node[p1-1][1],node[p2-1][1],node[p3-1][1],node[p1-1][1]]
        y = [node[p1-1][2],node[p2-1][2],node[p3-1][2],node[p1-1][2]]
        plt.plot(x, y)
    plt.axis('equal')
    
    
def barycentre(pt_intersection,n):
    x = 0
    y = 0 
    for i in range(n):
        x = x + pt_intersection[i][0]
        y = y + pt_intersection[i][1]
    return(x/float(n),y/float(n))

   
    
(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("m1.msh")
(nodes2, elems2, n_nodes_2, n_elems_2) = mshToPython_triangle("m2.msh")

#dessine_python(nodes1,elems1)
#dessine_python(nodes2,elems2)

  

nodes3 = []
elems3 = []
n_elems_3 = 0
nodes3 = []
n_nodes_3 = n_nodes_1 

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
                R = intersection(t1,t2,s1,s2)
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
                                
                                

#dessine_python(nodes3,elems3)
print nodes3
tab_remplace = []
for i in range(n_nodes_3):
    tab_remplace.append(-1)
#enleve les doublons
for i in range(n_nodes_3):
    for j in range(i+1,n_nodes_3):
        if((nodes3[i][1]==nodes3[j][1] and nodes3[i][2]==nodes3[j][2]) or (nodes3[i][1]==nodes3[j][2] and nodes3[i][2]==nodes3[j][1])):
            if(nodes3[i][1]!=-1 and nodes3[i][2]!=-1):    
                nodes3[j] = [-1,-1,-1,-1]
                tab_remplace[j] = i +1 #attention -nb_elem_sup

nb_elem_sup = 0
i = 0               
while(i < n_nodes_3-nb_elem_sup ):
    if(nodes3[i][0] == -1):
        del nodes3[i]
        nb_elem_sup = nb_elem_sup +1
        for j in range(n_nodes_3):
            if(tab_remplace[j]>i):
               tab_remplace[j] = tab_remplace[j] -1 
    
    else:
        i = i+1

        
for i in range(n_elems_3):
    for j in range(3):
        if(tab_remplace[elems3[i][j+1]-1]!=-1): #attention tab_remplace[elems3[i][j+1]]-1+1
            #print 'tada'
            #print tab_remplace[elems3[i][j+1]-1]
            #print elems3
            elems3[i][j+1] = tab_remplace[elems3[i][j+1]-1] #attention + 1 - 1

dessine_python(nodes3,elems3)