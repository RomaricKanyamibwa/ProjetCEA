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


node = [[0,0,0],[0,1,0],[1,1,0],[1,0,0],[0,1,1],[1,1,1],[0,0,1],[1,0,1]]
x = []
y = []
z = []
for i in range(len(node)):
	x.append(node[i][0])
	y.append(node[i][1])
	z.append(node[i][2])
xv, yv = np.meshgrid(y, x)

# build low-bandwidth numpy matrix
G = nx.grid_2d_graph(len(node), len(node))
ordering = [(y,len(node)-1-x) for y in range(len(node)) for x in range(len(node))]                      
labels = dict(zip(ordering, range(len(ordering)))) 
nx.draw(G)
plt.show()
rcm = list(reverse_cuthill_mckee_ordering(G))
print("ordering", rcm)


