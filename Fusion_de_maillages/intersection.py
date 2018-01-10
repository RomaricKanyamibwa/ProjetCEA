# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:18:43 2018
La fonction intersection prend en argument les deux triangles, les deux segments, et les tableaux de noeuds et de triaangle des deux maillages pour dire si ces segments se croise ou non, s'ils se croisent il renvoient les coordonnees 
"""

from mshToPython_triangle import *


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
        
        
def intersection(t1,t2,s1,s2,informations):
   nodes1 = informations[0]
   elems1 = informations[1]
   nodes2 = informations[2]
   elems2 = informations[3]
        
   p11 = [nodes1[elems1[t1][s1+1]-1][1],nodes1[elems1[t1][s1+1]-1][2],elems1[t1][s1+1]] #coordonées du point et numéro du point
   p12 = [nodes1[elems1[t1][(s1+1)%3+1]-1][1],nodes1[elems1[t1][(s1+1)%3+1]-1][2],elems1[t1][(s1+1)%3+1]]
   p21 = [nodes2[elems2[t2][s2+1]-1][1],nodes2[elems2[t2][s2+1]-1][2],elems2[t2][s2+1]]
   p22 = [nodes2[elems2[t2][(s2+1)%3+1]-1][1],nodes2[elems2[t2][(s2+1)%3+1]-1][2],elems2[t2][(s2+1)%3+1]]
   L1 = line(p11,p12)
   L2 = line(p21,p22)    
   R = intersect(L1,L2,p11,p12,p21,p22,s1,s2)
   return R

