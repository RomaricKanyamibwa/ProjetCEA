# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:16:18 2018

Renvoie le barycentre de n points d'intersections contenus dans ka liste pt_intersection
"""

def barycentre(pt_intersection,n):
    x = 0
    y = 0 
    for i in range(n):
        x = x + pt_intersection[i][0]
        y = y + pt_intersection[i][1]
    return(x/float(n),y/float(n))