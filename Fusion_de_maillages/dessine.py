# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:46:53 2017

@author: 3415249
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

deux_d = False

# Ouverture d'un fichier en *lecture*:
fichier = open("disque.msh")
 
# ...
# Utilisation du fichier
 
a = fichier.readline().split() # '$Nodes\n'

while(a[0]!="$Nodes"):
    a = fichier.readline().split() # '$Nodes\n'

n_nodes = int(fichier.readline()) # '8\n'


nodes = np.fromfile(fichier,count=n_nodes*4, sep=" ").reshape((n_nodes,4))
# array([[ 1. , -0.5, -0.5, -0.5],
#   [ 2. ,  0.5, -0.5, -0.5],
#   [ 3. , -0.5,  0.5, -0.5],
#   [ 4. ,  0.5,  0.5, -0.5],
#   [ 5. , -0.5, -0.5,  0.5],
#   [ 6. ,  0.5, -0.5,  0.5],
#   [ 7. , -0.5,  0.5,  0.5],
#   [ 8. ,  0.5,  0.5,  0.5]])

fichier.readline() # '$EndNodes\n'
fichier.readline() # '$Elements\n'
n_elems = int(fichier.readline()) # '2\n'

if(deux_d==False):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

for line in fichier:
    ligne = line.split(' ')
    #print ligne[1]
    len(ligne)
    if(len(ligne)>1):
        
        if(int(ligne[1])==2):
            nb_arg = int(ligne[2]) +1
            p1 = int(ligne[2+nb_arg]) - 1
            p2 = int(ligne[2+nb_arg+1]) -1
            p3 = int(ligne[2+nb_arg+2]) -1
            #print p1,p2,p3
            if(deux_d):
                #print nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]
                #print nodes[p1][2],nodes[p2][2],nodes[p3][2],nodes[p1][2]
                x = [nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]]
                y = [nodes[p1][2],nodes[p2][2],nodes[p3][2],nodes[p1][2]]
                plt.plot(x, y)
                plt.axis('equal')   # ajout
            else:
                #print nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]
                #print nodes[p1][2],nodes[p2][2],nodes[p3][2],nodes[p1][2]
                x = [nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]]
                y = [nodes[p1][2],nodes[p2][2],nodes[p3][2],nodes[p1][2]]
                z = [nodes[p1][3],nodes[p2][3],nodes[p3][3],nodes[p1][3]]
                ax.plot(x, y, z, '-b')
                ax.axis('equal')   # ajout
plt.show()

fichier.close()
"""
for i in range(14):
    fichier.readline()
elems = np.fromfile(fichier,count=(n_elems-14)*8,sep=" ").reshape((n_elems-14,8)) # $EndElements read as -1
# This array must be reshaped based on the element type(s)
# array([  1.,   4.,   2.,   1.,  11.,   1.,   2.,   3.,   5.,   2.,   4.,
#    2.,   1.,  11.,   2.,   5.,   6.,   8.])
# ...
print n_elems, n_nodes  

#for i in range(n_elems):
    #print elems[i]

# Fermeture du fichier
fichier.close()

for i in range(n_elems-14):
    nb_arg = elems[i][2] +1
    p1 = elems[i][2+nb_arg] -1
    p2 = elems[i][2+nb_arg+1] -1
    p3 = elems[i][2+nb_arg+2] -1
    print p1,p2,p3
    print nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]
    print nodes[p1][2],nodes[p2][2],nodes[p3][2],nodes[p1][2]
    x = [nodes[p1][1],nodes[p2][1],nodes[p3][1],nodes[p1][1]]
    y = [nodes[p1][1],nodes[p2][2],nodes[p3][2],nodes[p1][2]]
    plt.plot(x, y)
    plt.axis('equal')   # ajout
    plt.show()
    plt.close()
    
    
print "eeeeeeeeee"
plt.plot([0.500000000001, 0.0, 0.25, 0.500000000001],[1.0, 1.0, 0.75, 1.0])

"""



