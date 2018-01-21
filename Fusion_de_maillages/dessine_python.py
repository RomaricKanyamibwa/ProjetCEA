# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:11:08 2018
prend en argument un tableau de noeuds et un tableau de triangle et affiche la figure que ce maillage représente sous python
"""

from matplotlib import pyplot as plt

def dessine_python(node,elem,coul):
    for i in range(len(elem)):    
        p1 = int(elem[i][1])
        p2 = int(elem[i][2])
        p3 = int(elem[i][3])
        x = [node[p1-1][1],node[p2-1][1],node[p3-1][1],node[p1-1][1]]
        y = [node[p1-1][2],node[p2-1][2],node[p3-1][2],node[p1-1][2]]
        plt.plot(x, y,coul)
    plt.axis('equal')