# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:14:35 2018
@author: HAKAM Sophia,VOISEMBERT Colette,NDAYE Ramatoulaye, KANYAMIBWA Romaric
Homological group calculation
================
Calculation of the 2nd-Homological group of a 3D solid using Sympy and Smiths Normal Form
"""

#############################################################################
#  Copyright (C) 2017                                                       #
#                                                                           #
#                                                                           #
#  Distributed under the terms of the GNU General Public License (GPL)      #
#  either version 3, or (at your option) any later version                  #
#                                                                           #
#  http://www.gnu.org/licenses/                                             #
#############################################################################
import numpy as np
from numpy.linalg import matrix_rank
#from scipy import linalg
from sympy import *
from smith_normal_form import smith_form,smith_solve
import sys
import time
from sympy.matrices import SparseMatrix


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


def get_kerM_ImM_svd(A:SparseMatrix,B:SparseMatrix):
    AT_A=np.matrix(np.transpose(A))*np.matrix(A)
    B_BT=np.matrix(B)*np.matrix(np.transpose(B))
    M=AT_A+B_BT
    U,s,Vh = linalg.svd(M)
    r=matrix_rank(M)
    ImM=[0]*r
    KerM=[0]*(Vh.shape[0]-r)
    Um=SparseMatrix(U)
    Vm=SparseMatrix(Vh)
    for i in range(r):
        #print(i)
        #print(r)
        ImM[i]=Um.col(i)
        #tot=Um.col(i)
    for j in range(Vh.shape[0]-r):
        #if(i==0):
        KerM[j]=Vm.T.col(r+j)
        #ps = KerM[j].dot(tot)
        #print("ui*vj=",round(ps))
        #print("Real value:",ps)
        if(j>0):
            print("ui.ui-1=",KerM[j].dot(KerM[j-1]))
    return ImM,KerM,np.matrix(KerM).shape[0]
""""
ImM,KerM,Betti_number=get_kerM_ImM_svd(A,B)
print("ImM")
pprint(ImM)
#AT_A=np.matrix(np.transpose(A))*np.matrix(A)
#B_BT=np.matrix(B)*np.matrix(np.transpose(B))
#M=AT_A+B_BT
print("KerM:")
#for i in range(Vh.shape[0]-r):
#    KerM[i]=np.transpose(Vh)[r+i]
pprint(KerM)
#Betti_number=np.matrix(KerM).shape[0]
print("Nombre de betti",Betti_number)
"""

#------------------------------------------------Calcul avec la Forme Normal de Smith------------------------------------------------
def get_kerM_ImM_snf(A:SparseMatrix,B:SparseMatrix):
    M=A.T*A+B*B.T
    ncols = M.shape[1]
    b=[0]*ncols
    #An,L,R,r=smith_form(M)
    sol,An,L,R,r=smith_solve(M, b,True)
    ImM_SNF=[0]*r
    Linv=L.inv()
    for i in range(r):
        #print(i)
        #print(r)
        ImM_SNF[i]=Linv.col(i)
    #ImM_SNF=Linv.columnspace()
    #pprint(Linv.columnspace())
    #tot = L.inv().col(i)
    #print("ImM")
    #print(ImM_SNF)
    symbol=sol.free_symbols
    Betti_number_SNF=(R.inv().T.shape[0]-r)
    d={}
    vect=[0]*ncols
    KerM_SNF=[0]*Betti_number_SNF
    list_d=[{}]*Betti_number_SNF
    for k in range(Betti_number_SNF):
        counter=0
        for x in symbol:
            #print("subs")
            if counter==k :
                d[str(x)]=1
            else:
                d[str(x)]=0
            counter=counter+1
            #print(type(x),"=>",x)
        list_d[k]=d.copy()
    #pprint(list_d)
    i=0
    for k in range(Betti_number_SNF):
        vect=[0]*ncols
        i=0
        for elem in sol:
            vect[i]=elem.subs(list_d[k])
            #print(i,":",elem.subs(list_d[k]))
            i=i+1
        KerM_SNF[k]=SparseMatrix(vect).copy()
    #pprint(KerM_SNF)
    return M,r,ImM_SNF,KerM_SNF,Betti_number_SNF


def Select_Kernel_Method(A:SparseMatrix,B:SparseMatrix,method=2,display=false):
    print(A.shape)
    print(B.shape)
    if(method==1):
        start_time = time.time()
        M,r,ImM_SNF,KerM_SNF,Betti_number_SNF=get_kerM_ImM_snf(SparseMatrix(A),SparseMatrix(B))
        print("With smithsolve --- %s seconds ---" % (time.time() - start_time))
    if(method==2):#this method in general is faster
        M=A.T*A+B*B.T
        start_time = time.time()
        An,L,R,r = smith_form(M)
        #W=R
        Betti_number_SNF=(R.shape[0]-r)
        KerM_SNF=[0]*Betti_number_SNF
        for i in range(Betti_number_SNF):
            KerM_SNF[i]=R.col(r+i)
        print("With SNF --- %s seconds ---" % (time.time() - start_time))
    if(method==3):#this method in general is faster
        M=A.T*A+B*B.T
        start_time = time.time()
        KerM_SNF=M.nullspace()
        Betti_number_SNF=len(KerM_SNF)
        print("Nullspace --- %s seconds ---" % (time.time() - start_time))
    if(display):
        print("KerM_SNF:")
        pprint(KerM_SNF)
        print("Betti number:",Betti_number_SNF)
    #print("KerM with Nullspace")
    #start_time = time.time()
    #(M.nullspace())
    #print("With nullspace --- %s seconds ---" % (time.time() - start_time))
    #for x in KerM_SNF:
    #        pprint(M*x)
    return Betti_number_SNF,KerM_SNF


    #print("ps:")
#for j in range(R.inv().T.shape[0]-r):
    #if(i==0):
    #KerM_SNF[j]=R.inv().T.col(r+j)
    #nm=KerM_SNF[j].norm()*KerM[j].norm()
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

"""
M,r,ImM_SNF,KerM_SNF,Betti_number_SNF=get_kerM_ImM_snf(Matrix(A),Matrix(B))
print("ImM_SNF")
pprint(ImM_SNF)
print("ImM with Columnspace")
pprint(M.columnspace())
print("KerM_SNF:")
pprint(KerM_SNF)
print("KerM with Nullspace")
pprint(M.nullspace())
"""
#print("M=AT_A+B_BT:")
#pprint(Matrix(M))


#print("Nombre de betti with SNF",Betti_number_SNF)
#ncols = M.shape[1]
#b=[0]*ncols
#M=Matrix(M)
#print(M.shape)
#print(ncols)
#pprint(b)
#cols = len(M.row(0))
#sol=smith_solve(M, b)
#print(type(sol))
#pprint(sol)
#y15=1
#pprint(eval(str(sol[0])))
#pprint(type(sol[0]))
#ymbol=sol.free_symbols
#pprint(symbol)
"""
d={}
vect=[0]*ncols
KerM_SNF=[0]*Betti_number_SNF
list_d=[{}]*Betti_number_SNF
for k in range(Betti_number_SNF):
    counter=0
    for x in symbol:
        print("subs")
        if counter==k :
            d[str(x)]=1
        else:
            d[str(x)]=0
        counter=counter+1
        print(type(x),"=>",x)
    list_d[k]=d.copy()
pprint(list_d)
#sol.subs(d)
i=0
for k in range(Betti_number_SNF):
    vect=[0]*ncols
    i=0
    for elem in sol:
        vect[i]=elem.subs(list_d[k])
        print(i,":",elem.subs(list_d[k]))
        i=i+1
    KerM_SNF[k]=Matrix(vect).copy()
pprint(KerM_SNF)
KerM_ent=Matrix([-5, 0, -21, 16, 5, 16, -5, 0, 5, 6, -3, 4, -1, 4, 6,-1])
"""
#for i in range(r):
#    print(i,":ps=",KerM_SNF[0].dot(ImM_SNF[i]))
#    print(i,":ps_svd=",KerM_ent.dot(ImM[i]))
#print("ps_svd=",KerM_ent.dot(KerM[0]))
#print((KerM_ent.norm())*Matrix(KerM[0]).norm())
#m = M, Matrix(b)
#pprint(linsolve(m, symbols("y:" + str(cols))))

#for x in KerM_SNF:
#    pprint(M*x)

disp=False
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage example:python3 homology_calc.py [1|2] ")
    else:
        #if (len(sys.argv) >= 3):
        #disp=True
        print("Argv:",sys.argv[1])
        Select_Kernel_Method(SparseMatrix(A),SparseMatrix(B),int(sys.argv[1]),True)
