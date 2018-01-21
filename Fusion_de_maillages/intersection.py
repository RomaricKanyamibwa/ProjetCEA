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
    #retourne les coordonnes des points d intersection et les points des segments qui s intersectent 

    if(L1[1]==0 and L2[1]==0):
        #print "colineaire"
        #print "infini"
        return False
    if(L1[1]!=0 and L2[1]!=0 and (L1[0]/float(L1[1])==L2[0]/float(L2[1]))): #colineaire
        #print "colineaire"
        return False
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    #print D,Dx,Dy
    if D != 0:
        x = Dx / float(D)
        y = Dy / float(D)
        #segment
        if(x<min(p11[0],p12[0]) or x<min(p21[0],p22[0]) or x>max(p11[0],p12[0]) or x>max(p21[0],p22[0]) or y<min(p11[1],p12[1]) or y<min(p21[1],p22[1]) or y>max(p11[1],p12[1]) or y>max(p21[1],p22[1])):         
            #print "seg"
            return False
        if((p11[0]==p21[0] and p11[1]==p21[1]) or (p12[0]==p21[0] and p12[1]==p21[1]) or (p11[0]==p22[0] and p11[1]==p22[1]) or (p12[0]==p22[0] and p12[1]==p22[1])):
            #print "sommet qui se croisent"
            return False
        return [x,y,p11[2],p12[2],p21[2],p22[2],s1,s2] #coordonees du point intersectio, numero de points  des sommets des segments
    else:
        #print "ne se croise pas"        
        return False
   
        
def intersection(t1,t2,s1,s2,informations): #T1,T2 indices pas num triangle
# intersection entre les segments s1 et s2 respectivement des triangles t1 et t2
   nodes1 = informations[0]
   elems1 = informations[1]
   nodes2 = informations[2]
   elems2 = informations[3]
        
   p11 = [nodes1[elems1[t1][s1+1]-1][1],nodes1[elems1[t1][s1+1]-1][2],elems1[t1][s1+1]] #coordonees du point et numero du point
   p12 = [nodes1[elems1[t1][(s1+1)%3+1]-1][1],nodes1[elems1[t1][(s1+1)%3+1]-1][2],elems1[t1][(s1+1)%3+1]]
   p21 = [nodes2[elems2[t2][s2+1]-1][1],nodes2[elems2[t2][s2+1]-1][2],elems2[t2][s2+1]]
   p22 = [nodes2[elems2[t2][(s2+1)%3+1]-1][1],nodes2[elems2[t2][(s2+1)%3+1]-1][2],elems2[t2][(s2+1)%3+1]]
   L1 = line(p11,p12)
   L2 = line(p21,p22)    
   R = intersect(L1,L2,p11,p12,p21,p22,s1,s2)
   #print "R" 
   #print R
   return R

