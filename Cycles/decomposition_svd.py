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




def real_to_discr_SVD(M):
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

#Res=real_to_disct_SVD(M)
#print(Res==M)

r=matrix_rank(M)
ImM=[0]*r
KerM=[0]*(Vh.shape[0]-r)
Um=Matrix(U)
Vm=Matrix(Vh)
for i in range(r):
    #print(i)
    #print(r)
    ImM[i]=Um.col(i)
    tot=Um.col(i)
for j in range(Vh.shape[0]-r):
    #if(i==0):
    KerM[j]=Vm.T.col(r+j)
    #ps = KerM[j].dot(tot)
    #print("ui*vj=",round(ps))
    #print("Real value:",ps)
    if(j>0):
        print("ui.ui-1=",KerM[j].dot(KerM[j-1]))
        
print("ImM")
pprint(ImM)

print("KerM:")
#for i in range(Vh.shape[0]-r):
#    KerM[i]=np.transpose(Vh)[r+i]

pprint(KerM)

Betti_number=np.matrix(KerM).shape[0]
print("Nombre de betti",Betti_number)

An,L,R,r=smith_form((Matrix(M)))


#------------------------------------------------Forme Normal de Smith------------------------------------------------

ImM_SNF=[0]*r
KerM_SNF=[0]*(L.inv().shape[0]-r)
for i in range(r):
    #print(i)
    #print(r)
    ImM_SNF[i]=L.inv().col(i)
    tot = L.inv().col(i)
    #print("ImM")
    #print(ImM_SNF)

    #print("ps:")
for j in range(R.inv().T.shape[0]-r):
    #if(i==0):
    KerM_SNF[j]=R.inv().T.col(r+j)
    nm=KerM_SNF[j].norm()*KerM[j].norm()
    #ps = tot.dot(R.inv().T.col(r+j))
    #print(ps)
        
#j=0
#print("dot prod:",KerM_SNF[j].dot(KerM[j]))
#print("norm*norm:",nm)
#print("Theta angle=",(KerM_SNF[j].dot(KerM[j])/nm))
#print("Equality",KerM_SNF[j].dot(KerM[j])==KerM_SNF[j].norm()*KerM[j].norm())

#print("L==L.inv:",L.inv()==L)
#for i in range(R.shape[0]-r):
#        ps = R.inv().col(r).dot(R.inv().col(r+i))
#        print("PS")
#        print(ps)
print("ImM_SNF")
print(ImM_SNF)
print("KerM_SNF:")
print(KerM_SNF)
print("M=AT_A+B_BT:")
#pprint(Matrix(M))


#pprint(Matrix(L))
#pprint(Matrix(L.inv()*An*R.inv()))
#print("M")
#pprint(Matrix(M))
Betti_number_SNF=np.matrix(KerM).shape[0]
print("Nombre de betti with SNF",Betti_number_SNF)
ncols = M.shape[0]
b=[0]*ncols
M=Matrix(M)
#print(M.shape)
#print(ncols)
#pprint(b)
cols = len(M.row(0))
sol=smith_solve(M, b)
pprint(sol)
y15=1
pprint(eval(str(sol[0])))
#pprint(type(sol[0]))
pprint(sol.free_symbols)

KerM_ent=Matrix([-5, 0, -21, 16, 5, 16, -5, 0, 5, 6, -3, 4, -1, 4, 6,-1])

for i in range(r):
    print(i,":ps=",KerM_ent.dot(ImM_SNF[i]))
    print(i,":ps_svd=",KerM_ent.dot(ImM[i]))
    
print(":ps_svd=",KerM_ent.dot(KerM[0]))
print((KerM_ent.norm())*Matrix(KerM[0]).norm())
#m = M, Matrix(b)
pprint(linsolve(M, symbols("y:" + str(cols))))

pprint(M*KerM_ent)


#pprint(Matrix(b))
#pprint(Matrix(M))
#pprint(smith_solve(Matrix(M), b))

#m = Matrix(M), Matrix(b)
#pprint(linsolve(m, symbols("y:" + str(cols))))

#pprint(Matrix(L.T))
#print("L_T*L")
#pprint(L.inv().T*L.inv())
#print("SNF")
#print("L.inv()")
#pprint(L.inv())"""