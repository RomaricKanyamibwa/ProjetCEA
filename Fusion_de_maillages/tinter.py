import numpy as np
from mshToPython_triangle import *
from neighbors import *
from intersection import *


from chargement_des_donnees import *

'''
#definition des tableaux noeuds, elems et voisins
(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("Fichier_MSH/m1.msh")
(nodes2, elems2, n_nodes_2, n_elems_2) = mshToPython_triangle("Fichier_MSH/m2.msh")
'''

voisin1 = neighbours(elems1)
del voisin1[0]
voisin2 = neighbours(elems2)
del voisin2[0]
informations = (nodes1,elems1,nodes2,elems2)
''' 
voisin1 = [[2,3],[1,7],[1,4,5],[3],[6,3],[7,5],[2,8,6],[7]]
voisin2 = [[2],[1,3,5],[2,4],[3,7],[6,2],[5,7],[6,8,4],[7]]
croise = [[0, 1], [1, 0], [2, 3], [2, 3], [6, 7], [6, 7], [5, 4], [5, 4]]
'''


                
def intersecte(t1,t2):
    R = False
    for s1 in range(3): # segments du triangle du maillage 1
        for s2 in range(3): # segments du triangle du maillage 2
            #print(s1,s2)
            R = intersection(t1,t2,s1,s2,informations)
            if(R):
                return True
    return False
                
def TinterT(msh1,msh2, voisin_m1, voisin_m2):
    len1 = len(msh1)
    len2 = len(msh2)
    intersect = [[] for i in range(len1)] #mailage 1    
    
    t1 = 0
    #on cherche un triangle dans le maillage 2 qui intersecte t1
    i = 0    
    while((i < len2) and (intersecte(t1,i) == False)):
        i = i+1

    t2 = i-1
    intersect[t1].append(t2)
            
         
    aParcourir = []
    #on parcours jusqu'au voisins des voisins des voisins pour voir ceux qui s'intersecte avec t1
    ni = len(voisin_m2[t2])
    for i in range(ni):
        aParcourir.append(voisin_m2[t2][i])
    
    #print(aParcourir)
    n_1 = 0
    for k in range(2):
        n = len(aParcourir) ##attention pas du debut dou le n_1
        for i in range(n_1,n):
            nj = len(voisin_m2[aParcourir[i]-1])
            for j in range(nj):
                if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                    aParcourir.append(voisin_m2[aParcourir[i]-1][j]) #attention n ou n-1
        n_1 = n
   
    #dans les voisins a parcourir on regarde ceux qui coupent t1
    for i in range(len(aParcourir)):
        if(intersecte(t1,aParcourir[i]-1)):
            if(aParcourir[i]-1 not in intersect[t1]):
                t2 = aParcourir[i]-1
                intersect[t1].append(t2)
         
    ## RECURRENCE     
    triangle1_coupe_triangle2 = [-1 for i in range(len1)]
    triangle1_coupe_triangle2[t1] = t2 # tableau qui recense le t2 dont on devra partir si on veut trouver le t2 qui coupe t1  
    aParcourir_maillage1 = []
    
    n_elems_parcourus = 1
    for i in range(len(voisin1[t1])):
        triangle1_coupe_triangle2[voisin1[t1][i]-1] = t2
        aParcourir_maillage1.append(voisin1[t1][i])
    #triangles1_ordres_parcours = [2,3,4,5,6,7,1] #########attention a faire
    
      
    while(n_elems_parcourus<len1):
        nb_a_supr = len(aParcourir_maillage1)
        n_elems_parcourus = n_elems_parcourus + nb_a_supr
        for l in range(nb_a_supr):  #choisir t1 attention
            ####################################trouver t2
            t1 = aParcourir_maillage1[l] -1
            #print "T1"
            #print t1, triangle1_coupe_triangle2
            nontrouve = True
            aParcourir = []
            t2 = triangle1_coupe_triangle2[t1] -1
            ni = len(voisin_m2[t2])
            for i in range(ni):
                aParcourir.append(voisin_m2[t2][i])
            n_1 = 0
            #print(aParcourir)
    
            for i in range(len(aParcourir)):
                if(intersecte(t1,aParcourir[i]-1)):
                    t2 = aParcourir[i]-1
                    intersect[t1].append(t2)
                    nontrouve = False
            
            
    
            while nontrouve:
                #print("non trouve")
                #print t1,t2
                n = len(aParcourir)
                for i in range(n_1,n):
                    nj = len(voisin_m2[aParcourir[i]-1])
                    for j in range(nj):
                        if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                            aParcourir.append(voisin_m2[aParcourir[i]-1][j])
                            if(intersecte(t1,voisin_m2[aParcourir[i]-1][j]-1)):
                                t2 = voisin_m2[aParcourir[i]-1][j]-1
                                intersect[t1].append(t2)
                                nontrouve = False                    
                    n_1 = n
                #print aParcourir
                   
            ######################################
            aParcourir = []
            #print(t1,t2)
            #on parcours 3 voisins de voisins
            ni = len(voisin_m2[t2])
            for i in range(ni):
                aParcourir.append(voisin_m2[t2][i])
            #print(aParcourir)
            n_1 = 0
            for k in range(2):
                n = len(aParcourir) ##attention pas du debut dou le n_1
                for i in range(n_1,n):
                    nj = len(voisin_m2[aParcourir[i]-1])
                    for j in range(nj):
                        if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                            aParcourir.append(voisin_m2[aParcourir[i]-1][j]) #attention n ou n-1
                n_1 = n
       
            #dans les voisins a parcourir on regarde ceux qui coupent t1
            for i in range(len(aParcourir)):
                if(intersecte(t1,aParcourir[i]-1)):
                    if(aParcourir[i]-1 not in intersect[t1]):
                        t2 = aParcourir[i]-1
                        intersect[t1].append(t2)  
                            
        for i in range(nb_a_supr):
            next_triangle = aParcourir_maillage1[0] -1
            for j in voisin1[next_triangle]:
                if(triangle1_coupe_triangle2[j-1] == -1): # si deja parcouru on ne le rajoute pas a la liste a parcourir
                    aParcourir_maillage1.append(j) #num de 1 a n
                    triangle1_coupe_triangle2[j-1] = next_triangle
            del aParcourir_maillage1[0]
            
    return intersect

croise = TinterT(elems1,elems2, voisin1, voisin2) # couple de triangles qui se croisent, le &er element est un numero de triangle (inice) du maillage 1 le second un du maillage 2def superposition(node1,node2,elems1,elems2, voisin1, voisin2, intersecte):
