# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:07:08 2018

"""

from numpy.linalg import matrix_rank

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
        

dim_Im_A2 = matrix_rank(A2)
n = size(A1)/len(A1)
dim_Ker_A1 = n - matrix_rank(A1) #rang theorem
print(dim_Ker_A1 - dim_Im_A2)