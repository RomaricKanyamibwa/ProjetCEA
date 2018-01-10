# -*- coding: utf-8 -*-
"""
Created on Tues Jan 9 18:44:29 2018

@author: colette
"""

import numpy as np
#import matplotlib.pyplot as plt


elem = [[1,2,3],[4,5,6]]
node = [[0,0,0],[2,0,0],[0,2,0],[0.5,0.5,0],[0.5,0.75,0],[0.75,0.5,0]]


def interieur(i,j):
#renvoie True si le trinagle i est contenu dans le triangle j ou le trinagle j dans le i
    P_BBp = [[0,0],[0,0]]

    #matrice de passage base de référence triangle i
    P_BBp[0][0] = node[elem[i][0]-1][0] - node[elem[i][1]-1][0]
    P_BBp[1][0] = node[elem[i][0]-1][1] - node[elem[i][1]-1][1]
    P_BBp[0][1] = -node[elem[i][1]-1][0] + node[elem[i][2]-1][0]
    P_BBp[1][1] = -node[elem[i][1]-1][1] + node[elem[i][2]-1][1]
    
    P_BBp_inv = np.linalg.inv(P_BBp)
    #print inter(P_BBp,j,i)
    #print inter(P_BBp_inv,i,j)
    return inter(P_BBp,j,i) or inter(P_BBp_inv,i,j)





def inter(P_BBp,j,k):
    #exprimer le trinagle 0 dans la base du triangle 1
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]
    for i in range(3):
        x = node[elem[j][i]-1][0] - node[elem[k][1]-1][0]  #si l'origine est décalée
        y = node[elem[j][i]-1][1] - node[elem[k][1]-1][1]
        Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
        Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
        x_b = Dx/D
        y_b = Dy/D
        if(x_b>1 or x_b<0 or y_b>1 or y_b<0 or x_b+y_b>1 or x_b+y_b<0):
            return False
    return True



print interieur(0,1)