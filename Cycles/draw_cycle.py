# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:06:39 2018

@author: colette
"""

def draw_cycle(vect, node, elem, arrete):
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    for i in range(len(elem)):    
        p1 = int(elem[i][0])
        p2 = int(elem[i][1])
        p3 = int(elem[i][2])
        x = [node[p1][0],node[p2][0],node[p3][0],node[p1][0]]
        y = [node[p1][1],node[p2][1],node[p3][1],node[p1][1]]
        z = [node[p1][2],node[p2][2],node[p3][2],node[p1][2]]
        ax.plot(x, y, z, 'g')
        ax.axis('equal')
    for i in range(len(vect)):
        if(vect[i]!=0):
            s1 = arrete[i][0][0]
            s2 = arrete[i][0][1]
            x = [node[s1][0],node[s2][0]]
            y = [node[s1][1],node[s2][1]]
            z = [node[s1][2],node[s2][2]]
            ax.plot(x, y, z, 'r')
            ax.axis('equal') 
plt.show()
