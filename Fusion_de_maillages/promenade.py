from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:37:17 2017
@author: HAKAM Sophia, VOISEMBERT Colette, KANYAMIBWA Romaric,NDAYE Ramatoulaye

================


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

from numpy import cross,arccos,dot,clip,arctan2
from numpy.linalg import det,norm
from math import pi
from neighbors import list_neighbors
from neighbors import neighbours



def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return arccos(clip(dot(v1_u, v2_u), -1.0, 1.0))


def angle_cclockwise(A, B):
    """
    fonction qui retourne l'angle de 2 vecteurs dans le sens trigonometrique
    """
    inner=angle_between(A,B)
    a=[A,B]
    d = det(a)
    if d<0: #this is a property of the det. If the det < 0 then B is clockwise of A
        return -inner
    else: # if the det > 0 then A is immediately clockwise of B
        return inner

def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = dot(v1, v2)
    sinang = norm(cross(v1, v2))
    return arctan2(sinang, cosang)

angle_between((1, 0, 0), (-1, 0, 0))

X1=[1.0, 1.0, 0.9375, 1.0]
Y1=[1.0, 0.875, 0.9375, 1.0]
X2=[1.0, 0.9375, 0.9375, 1.0]
Y2=[0.875, 0.8125, 0.9375, 0.875]

ez=[0,0,1] #vecteur unité 
def surface_triangle(p1,p2,p3,TwoDim=True):
    """pour l'instant on calcule l'aire en 2D"""
    S1=p1
    S3=p3
    S2=p2
    if(len(p1)<3):
        S1=S1+[0]
    if(len(p2)<3):
        S2=S2+[0]
    if(len(p3)<3):
        S3=S3+[0]    
    a=[-S1[0]+S2[0],-S1[1]+S2[1],-S1[2]+S2[2]]
    b=[S3[0]-S1[0],S3[1]-S1[1],S3[2]-S1[2]]
    #print("a:",a)
    #print("b",b)
    print(cross(a,b))
    res=dot(cross(a,b),ez)
    print("Dot:",res)
    #if(dot(cross(a,b),ez)>0):
    #if(TwoDim):
     #   a.pop()
      #  b.pop()  
    #surface=det([a,b])
    #print("surface:",det([a,b]))
    #print("surface2:",det([b,a]))
    #print("RES:",surface)
    return res


#♥surface_triangle([0,0],[1,0],[0,-1])   
#surface_triangle([0,0],[0,1],[0,-1])  
#surface_triangle([1,0],[0,1],[0,-1])
#print("")  
#print("triang non adj")
#print("")
#surface_triangle([0,0],[1,0],[2,0])   
#surface_triangle([0,0],[0,1],[2,0])  
#surface_triangle([0,1],[1,0],[2,0 ])  


def test_include_triang(p1,p2,p3,a,TwoDim=True):
    S1=surface_triangle(p1,p2,a)
    S2=surface_triangle(p1,p3,a)
    S3=surface_triangle(p2,p3,a)
    if(S1<0 or S2<0 or S3<0):
        print("YES")
        if(S1<0):
            return 2,3
        if(S2<0):
            return 2,4
        else:
            return 3,4
    print("NO")
    return True

test_include_triang([0,0],[1,0],[0,1],[0,1])
test_include_triang([0,0],[1,0],[0,1],[0,0.5])

it=0

def find_index(List,num):
    ind=0
    for i in List:
        if(num==i[0]):
            return ind
        ind=ind+1
    return False

def promenade(List_triang,List_point,point,num_triang):
    print("N°iteration:"+it)
    ind_triang= find_index(List_triang,num_triang)
    if(num_triang>len(List_triang)):
        raise ValueError("Valeur de triangle non definit")
    t=List_triang[ind_triang]
    p1=find_index(List_point,List_triang[t][1])
    p2=find_index(List_point,List_triang[t][2])
    p3=find_index(List_point,List_triang[t][3])
    k=test_include_triang(List_point[p1],List_point[p2],List_point[p3],point)
    if(k==True):
        return t
    else:
        
        max,neigh=list_neighbors(List_triang)
        if(neigh[(List_triang[t][k[0]],List_triang[t][k[1]])]==t):
            new_num_triang=neigh[1]
        else:
            new_num_triang=neigh[0]
        return promenade(List_triang,point,new_num_triang)
    
    
    

List_triang=[[1,1,2,3],[2,2,3,4],[3,1,3,5],[4,1,2,6]]
List_point=[[1,0,0],[2,1,1],[3,0,1],[4,1,2],[5,1,-1],[6,-1,1]]
neighbours(List_triang)
#promenade(List_triang,List_point,[-1,1])
# def promenade(List_triang,List_point,point,num_triang=0):
#     t=List_triang[num_triang]
#     if(test_include_triang(List_point[t-1][0],List_point[t-1][1],List_point[t-1][2],point)):
#         return t
#     else: 
#         neigh=neighbours(List_triang)
#         return promenade(neigh,List_point,point)


