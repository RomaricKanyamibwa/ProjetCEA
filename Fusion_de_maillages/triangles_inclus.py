# -*- coding: utf-8 -*-
"""
Created on Tues Jan 9 18:44:29 2018

@author: colette
"""

import numpy as np
from mshToPython_triangle import *
from chargement_des_donnees import *

def interieur(i,j):
#renvoie True si le trinagle i du maillage1 est contenu dans le triangle j du maillage2 ou le trinagle j dans le i, False sinon
    
    
    P_BBp = [[0,0],[0,0]]
    
    #matrice de passage base de référence triangle i
    P_BBp[0][0] = nodes1[elems1[i][1]-1][1] - nodes1[elems1[i][2]-1][1]
    P_BBp[1][0] = nodes1[elems1[i][1]-1][2] - nodes1[elems1[i][2]-1][2]
    P_BBp[0][1] = -nodes1[elems1[i][2]-1][1] + nodes1[elems1[i][3]-1][1]
    P_BBp[1][1] = -nodes1[elems1[i][2]-1][2] + nodes1[elems1[i][3]-1][2]
    
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]
    if(D==0):
        print "Attention erreur, déterminant nul dans la fontionintereur de triagles_inclus"

    
    P_BBp_inv = np.linalg.inv(P_BBp)
    
    return inter(P_BBp,j,i) or inter(P_BBp_inv,i,j)
    


def inter(P_BBp,j,k):
    #exprimer le trinagle 0 dans la base du triangle 1
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]
    for i in range(3):
        x = nodes2[elems2[j][i+1]-1][1] - nodes1[elems1[k][2]-1][1]  #si lorigine est décalee
        y = nodes2[elems2[j][i+1]-1][2] - nodes1[elems1[k][2]-1][2]
        
        Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
        Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
        x_b = Dx/D
        y_b = Dy/D
        if(x_b>1 or x_b<0 or y_b>1 or y_b<0 or x_b+y_b>1 or x_b+y_b<0):
            return False

    return True
    
def point_inter_triangle(x,y,i):
    #renvoie true si le point decoordonnees (x,y) est dans le triangle i du maillage 1, False sinon
    P_BBp = [[0,0],[0,0]]

    #matrice de passage base de reference triangle i
    P_BBp[0][0] = nodes1[elems1[i][1]-1][1] - nodes1[elems1[i][2]-1][1]
    P_BBp[1][0] = nodes1[elems1[i][1]-1][2] - nodes1[elems1[i][2]-1][2]
    P_BBp[0][1] = -nodes1[elems1[i][2]-1][1] + nodes1[elems1[i][3]-1][1]
    P_BBp[1][1] = -nodes1[elems1[i][2]-1][2] + nodes1[elems1[i][3]-1][2]
    
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]    
    
    x = x - nodes1[elems1[i][2]-1][1]  #si l'origine est décalée
    y = y - nodes1[elems1[i][2]-1][2]
    Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
    Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
    x_b = Dx/float(D)
    y_b = Dy/float(D)
    if(x_b>1 or x_b<0 or y_b>1 or y_b<0 or x_b+y_b>1 or x_b+y_b<0):
        return False
    return True

def point_inter_strict_triangle(x,y,i):
    #renvoie true si le point decoordonnees (x,y) est dans le triangle i du maillage 1, False sinon
    P_BBp = [[0,0],[0,0]]

    #matrice de passage base de reference triangle i
    P_BBp[0][0] = nodes1[elems1[i][1]-1][1] - nodes1[elems1[i][2]-1][1]
    P_BBp[1][0] = nodes1[elems1[i][1]-1][2] - nodes1[elems1[i][2]-1][2]
    P_BBp[0][1] = -nodes1[elems1[i][2]-1][1] + nodes1[elems1[i][3]-1][1]
    P_BBp[1][1] = -nodes1[elems1[i][2]-1][2] + nodes1[elems1[i][3]-1][2]
    
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]    
    
    x = x - nodes1[elems1[i][2]-1][1]  #si lorigine est décalee
    y = y - nodes1[elems1[i][2]-1][2]
    Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
    Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
    x_b = Dx/float(D)
    y_b = Dy/float(D)
    if(x_b>=1 or x_b<=0 or y_b>=1 or y_b<=0 or x_b+y_b>=1 or x_b+y_b<=0):
        return False
    return True
    
def point_inter_triangle_m2(x,y,i):
    #renvoie true si le point decoordonnees (x,y) est dans le triangle i du maillage 1, False sinon
    P_BBp = [[0,0],[0,0]]

    #matrice de passage base de reference triangle i
    P_BBp[0][0] = nodes2[elems2[i][1]-1][1] - nodes2[elems2[i][2]-1][1]
    P_BBp[1][0] = nodes2[elems2[i][1]-1][2] - nodes2[elems2[i][2]-1][2]
    P_BBp[0][1] = -nodes2[elems2[i][2]-1][1] + nodes2[elems2[i][3]-1][1]
    P_BBp[1][1] = -nodes2[elems2[i][2]-1][2] + nodes2[elems2[i][3]-1][2]
    
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]    
    
    x = x - nodes2[elems2[i][2]-1][1]  #si l'origine est décalée
    y = y - nodes2[elems2[i][2]-1][2]
    Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
    Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
    x_b = Dx/float(D)
    y_b = Dy/float(D)
    if(x_b>1 or x_b<0 or y_b>1 or y_b<0 or x_b+y_b>1 or x_b+y_b<0):
        return False
    return True

def point_inter_strict_triangle_m2(x,y,i):
    #renvoie true si le point decoordonnees (x,y) est dans le triangle i du maillage 1, False sinon
    P_BBp = [[0,0],[0,0]]

    #matrice de passage base de reference triangle i
    P_BBp[0][0] = nodes2[elems2[i][1]-1][1] - nodes2[elems2[i][2]-1][1]
    P_BBp[1][0] = nodes2[elems2[i][1]-1][2] - nodes2[elems2[i][2]-1][2]
    P_BBp[0][1] = -nodes2[elems2[i][2]-1][1] + nodes2[elems2[i][3]-1][1]
    P_BBp[1][1] = -nodes2[elems2[i][2]-1][2] + nodes2[elems2[i][3]-1][2]
    
    D = P_BBp[0][0]*P_BBp[1][1] - P_BBp[1][0]*P_BBp[0][1]    
    
    x = x - nodes2[elems2[i][2]-1][1]  #si l'origine est décalée
    y = y - nodes2[elems2[i][2]-1][2]
    Dx = x*P_BBp[1][1] - y*P_BBp[0][1]
    Dy = P_BBp[0][0]*y - P_BBp[1][0]*x
    x_b = Dx/float(D)
    y_b = Dy/float(D)
    if(x_b>1 or x_b<0 or y_b>1 or y_b<0 or x_b+y_b>1 or x_b+y_b<0):
        return False
    return True
