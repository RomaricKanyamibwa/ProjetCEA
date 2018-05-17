# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:07:08 2018

"""

from numpy.linalg import matrix_rank
from draw_cycle import *

node = [[0,0,0],[0,1,0],[1,1,0],[1,0,0],[0,1,1],[1,1,1],[0,0,1],[1,0,1]]
elem = [[1,0,3], [1,3,2],[4,1,2],[4,2,5],[4,5,6],[6,5,7],[0,6,7],[0,7,3]]

#avec deux fois plus de triangles

node = [[0,0,0],[0,1,0],[1,1,0],[1,0,0],[0,1,1],[1,1,1],[0,0,1],[1,0,1],[],[],[],[]]
elem = [[8,0,3], [8,0,1],[8,1,2],[3,2,8],[1,2,9],[1,4,9],[4,5,9],[2,5,9],[4,5,10],[4,6,10],[6,7,10],[5,7,10],[6,7,11],[6,0,11],[0,3,11],[3,7,11]]

        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
A1 = [  [ 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1],
        [ 0, 1,-1, 0,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 1, 1, 0, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 1, 0, 0, 0,-1, 1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1, 0, 0,-1, 1]]
        
A2 = [  [-1, 0, 0, 0, 0, 0, 0, 1],
        [-1, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 1,-1, 0, 0, 0, 0, 0],
        [ 0, 1, 0, 0, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0, 0],
        [ 0, 0,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 1,-1, 0, 0, 0],
        [ 0, 0, 0, 1, 0, 0, 0, 0],
        [ 0, 0,-1, 1, 0, 0, 0, 0],
        [ 0, 0, 0, 0,-1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 1,-1, 0],
        [ 0, 0, 0, 0, 0, 1, 0, 0],
        [ 0, 0, 0, 0,-1, 1, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 1],
        [ 0, 0, 0, 0, 0, 0,-1, 1]]
        

#dim_Im_A2 = matrix_rank(A2)
#n = size(A1)/len(A1)
#dim_Ker_A1 = n - matrix_rank(A1) #rang theorem
#print(dim_Ker_A1 - dim_Im_A2)


#draw_cycle([], node, elem, [])
