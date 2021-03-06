#!/usr/bin/python
"""
===
Rcm
===

Cuthill-McKee ordering of matrices

The reverse Cuthill-McKee algorithm gives a sparse matrix ordering that
reduces the matrix bandwidth.
"""

import networkx as nx
from networkx.utils import reverse_cuthill_mckee_ordering
import numpy as np
import matplotlib.pyplot as plt


node = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
arete = [[(0, 1), [0]], [(5, 6), [4, 5]], [(5, 7), [5]], [(3, 7), [7]], [(4, 5), [3, 4]], [(6, 7), [5, 6]], [(4, 6), [4]], [(0, 3), [0, 7]], [(0, 7), [6, 7]], [(1, 2), [1, 2]], [(2, 5), [3]], [(0, 6), [6]], [(1, 4), [2]], [(2, 3), [1]], [(1, 3), [0, 1]], [(2, 4), [2, 3]]]

x = []
y = []
z = []
for i in range(len(node)):
	x.append(node[i][0])
	y.append(node[i][1])
	z.append(node[i][2])
G = nx.Graph()
for i in range(len(node)):
	G.add_node(i, x=x[i], y=y[i], z=z[i])
	
# aretes:
for i in range(len(arete)):
	G.add_edge(arete[i][0][0],arete[i][0][1])
	
'''
G.add_edge(3,0)
G.add_edge(0,1)
G.add_edge(2,1)
G.add_edge(3,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(5,4)
G.add_edge(2,5)
G.add_edge(4,2)
G.add_edge(4,6)
G.add_edge(7,6)
G.add_edge(5,7)
G.add_edge(6,5)
G.add_edge(6,0)
G.add_edge(7,3)
G.add_edge(0,7)
'''
print(G.nodes(data=True))

nx.draw(G)
plt.show()
rcm = list(reverse_cuthill_mckee_ordering(G))
print("ordering", rcm)

node_res = []
for i in range(len(rcm)):
	node_res.append([G.node[rcm[i]]['x'],G.node[rcm[i]]['y'],G.node[rcm[i]]['z']])
print(node_res)
