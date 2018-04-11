import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

deux_d = False

node = []
#[[0,0,0],[3,0,0],[3,0,3],[0,0,3],
#        [1,0,1],[2,0,1],[2,0,2],[1,0,2],
#        [1,0,1],[2,0,1],[1,0,3],[2,0,3],
#        [0,3,0],[3,3,0],[3,3,3],[0,3,3],
#        [1,3,1],[2,3,1],[2,3,2],[1,3,2],
#        [1,3,1],[2,3,1],[1,3,3],[2,3,3]]

elem1 = []

#[[0,8,10],[0,30,10],[4,8,5],[7,10,11],[8,9,5],[7,6,11],[9,1,2],[9,2,11],
#        [12,20,22],[12,22,15],[20,17,16],[18,23,22],[20,21,17],[18,19,23],[21,13,14],[21,14,23],
#        [12,13,14],[12,1,0],[13,14,2],[13,2,1],[15,14,2],[15,2,13],[12,15,3],[12,3,0],
#        [16,17,4],[17,4,5],[17,19,5],[19,6,5],[18,19,7],[19,6,7],[16,18,4],[18,7,4]]


def nb_holes(n):
    for i in range(0,n):
        node.append([0+i*3,0,0])
        node.append([3+i*3,0,0])
        node.append([3+i*3,0,3])
        node.append([0+i*3,0,3])
        node.append([1+i*3,0,1])
        node.append([2+i*3,0,1])
        node.append([2+i*3,0,2])
        node.append([1+i*3,0,2])
        node.append([1+i*3,0,1])
        node.append([2+i*3,0,1])
        node.append([1+i*3,0,3])
        node.append([2+i*3,0,3])
        node.append([0+i*3,3,0])
        node.append([3+i*3,3,0])
        node.append([3+i*3,3,3])
        node.append([0+i*3,3,3])
        node.append([1+i*3,3,1])
        node.append([2+i*3,3,1])
        node.append([2+i*3,3,2])
        node.append([1+i*3,3,2])
        node.append([1+i*3,3,1])
        node.append([2+i*3,3,1])
        node.append([1+i*3,3,3])
        node.append([2+i*3,3,3])

        elem1.append([0+i*24,8,10])
        elem1.append([0+i*24,30,10])
        elem1.append([4+i*24,8,5])
        elem1.append([7+i*24,10,11])
        elem1.append([8+i*24,9,5])
        elem1.append([7+i*24,6,11])
        elem1.append([9+i*24,1,2])
        elem1.append([9+i*24,2,11])
        elem1.append([12+i*24,20,22])
        elem1.append([12+i*24,22,15])
        elem1.append([20+i*24,17,16])
        elem1.append([18+i*24,23,22])
        elem1.append([20+i*24,21,17])
        elem1.append([18+i*24,19,23])
        elem1.append([21+i*24,13,14])
        elem1.append([21+i*24,14,23])
        elem1.append([12+i*24,13,1])
        elem1.append([12+i*24,1,0])
        elem1.append([15+i*24,14,2])
        elem1.append([15+i*24,2,13])
        elem1.append([12+i*24,15,3])
        elem1.append([12+i*24,3,0])
        elem1.append([16+i*24,17,4])
        elem1.append([17+i*24,4,5])
        elem1.append([17+i*24,19,5])
        elem1.append([19+i*24,6,5])
        elem1.append([18+i*24,19,7])
        elem1.append([19+i*24,6,7])
        elem1.append([16+i*24,18,4])
        elem1.append([18+i*24,7,4])


        if(i == n):
            elem1.append([13+i*24,14,2])
            elem1.append([13+i*24,2,1])



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

draw_cycle([], node, elem1, [])
nb_holes(2)
plt.show()