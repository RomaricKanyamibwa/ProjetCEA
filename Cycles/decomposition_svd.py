# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:14:35 2018

@author: 3600594
"""
import numpy as np
from numpy.linalg import matrix_rank
from scipy import linalg
from sympy import *
from smith_normal_form import smith_form,smith_solve
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
A = [   [ 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1],
        [ 0, 1,-1, 0,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 1, 1, 0, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 1, 0, 0, 0,-1, 1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1, 0, 0,-1, 1]]
        # 1  2  3  4  5  6  7  8
B = [   [-1, 0, 0, 0, 0, 0, 0, 1],
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



Nv=8#Nombre de sommet
Ne=16#Nombre d'arretes
Nt=8# Nombre de Triangle


#R^16=Im(B)+Im(B_ortho)




AT_A=np.matrix(np.transpose(A))*np.matrix(A)
B_BT=np.matrix(B)*np.matrix(np.transpose(B))

M=AT_A+B_BT

U,s,Vh = linalg.svd(M)




def real_to_disct_SVD(M):
    U,s,V = linalg.svd(M)
    m=U.shape
    n=V.shape
    S=np.zeros((m[0], n[0]))
    S[:n[0], :n[0]] = np.diag(s)
    M_re=np.dot(U, np.dot(S, V))
    #print("S=>")
    #print(U)
    #print("M=>")
     #print(M_re)
    return  np.rint(M_re)

Res=real_to_disct_SVD(M)
#print(Res==M)

r=matrix_rank(M)
ImM=[0]*r
KerM=[0]*(U.shape[0]-r)
for i in range(r):
    #print(i)
    #print(r)
    ImM[i]=np.transpose(U)[i]
print("ImM")
print(ImM)

print("KerM:")
for i in range(U.shape[0]-r):
    KerM[i]=np.transpose(U)[r+i]

print(KerM)

Betti_number=np.matrix(KerM).shape[0]
An,L,R,r=smith_form((Matrix(M)))

print("Nombre de betti",Betti_number)

print("L,L_T")
#pprint(Matrix(L))
#pprint(Matrix(L.inv()*L))
cols = M.shape[0]
b=[0]*cols
pprint(Matrix(b))
pprint(Matrix(M))
pprint(smith_solve(Matrix(M), b))

#m = Matrix(M), Matrix(b)
#pprint(linsolve(m, symbols("y:" + str(cols))))

#pprint(Matrix(L.T))
#print("L_T*L")
#pprint(L.inv().T*L.inv())
#print("SNF")
#print("L.inv()")
#pprint(L.inv())


