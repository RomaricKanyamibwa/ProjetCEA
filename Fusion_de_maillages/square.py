from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:49:51 2017
@author: HAKAM Sophia, VOISEMBERT Colette, KANYAMIBWA Romaric,NDAYE Ramatoulaye

Generate Meshed Polygons
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


from matplotlib import pyplot as plt
from math import cos,sin,pi



def square(k,fig=1):
    plt.figure(fig)
    n=k//2+1
    nodes=list(range(0,n));
    listp=[]
    
    #decoupage du carré
    for j in nodes:
        
        if((([n-1,j],[0,j]) not in listp) and (n-j!=0) and (([0,j],[n-1,j]) not in listp)):
            x = [n-1,0]
            plt.plot(x,[j,j])
            listp+=[([n-1,j],[0,j])]
            
        if(([0,0],[0,j]) not in listp  and (j!=0) and (([0,j],[0,0]) not in listp )):
            x = [0,0]
            plt.plot(x,[0,j])
            #if([0,0] not in listp):
            listp+=[([0,0],[0,j])]
            
        if(([0,0],[n-1,0]) not in listp  and (n-1!=0) and (([n-1,0],[0,0]) not in listp)):   
            x = [0,n-1]
            plt.plot(x,[0,0])
            #if([n-1,0] not in listp):
            listp+=[([0,0],[n-1,0])]
            
        if(([n-1,0],[n-1,j]) not in listp  and (j!=0) and (([n-1,j],[n-1,0]) not in listp)):
            x = [n-1,n-1]
            plt.plot(x,[0,j])
            listp+=[([n-1,0],[n-1,j])]
    triang=0
    nodes=list(range(1,n));
    for j in nodes:
        if(([n-1,j-1],[0,j]) not in listp and ([0,j],[n-1,j-1]) not in listp):   
            x = [n-1,0]
            plt.plot(x,[j-1,j])
            listp+=[([n-1,j-1],[0,j])]
            triang+=1
    triang*=2
    if(k%2==1):
        x = [n-1,(n-1)/2]
        plt.plot(x,[n-1,(2*n-3)/2])
        #print([n-1,(2*n-3)/2])
        listp+=[([n-1,n-1],[(n-1)/2,(2*n-3)/2])]
        triang+=1
        
#        x = [0,0]
#        plt.plot(x,[0,j])
#        if([0,0] not in listp):
#            listp+=[[0,0]]
#        
#        x = [0,n-1]
#        plt.plot(x,[0,0])
#        if([n-1,0] not in listp):
#            listp+=[[n-1,0]]
#        
#        x = [n-1,n-1]
#        plt.plot(x,[0,j])
        #listp+=[[n-1,0],[n-1,n-1]]
    #listp=list(set(listp))
    print(listp)
    print(triang)   
    print(len(listp))
    plt.axis('equal')
    plt.show()
    return listp
    

def square2(k,fig=2):
    plt.figure(fig)
    n=k//2+1
    nodes=list(range(0,n));
    listp=[]
    
    #decoupage du carré
    for j in nodes:
        
        if((([n-1,j],[0,j]) not in listp) and (n-j!=0) and (([0,j],[n-1,j]) not in listp)):
            x = [n-1,0]
            plt.plot(x,[j,j])
            listp+=[([n-1,j],[0,j])]
            
        if(([0,0],[0,j]) not in listp  and (j!=0) and (([0,j],[0,0]) not in listp)):
            x = [0,0]
            plt.plot(x,[0,j])
            #if([0,0] not in listp):
            listp+=[([0,0],[0,j])]
            
        if(([0,0],[n-1,0]) not in listp  and (n-1!=0) and (([n-1,0],[0,0]) not in listp )):   
            x = [0,n-1]
            plt.plot(x,[0,0])
            #if([n-1,0] not in listp):
            listp+=[([0,0],[n-1,0])]
            
        if(([n-1,0],[n-1,j]) not in listp  and (j!=0) and (([n-1,j],[n-1,0]) not in listp)):
            x = [n-1,n-1]
            plt.plot(x,[0,j])
            listp+=[([n-1,0],[n-1,j])]
    triang=0
    nodes=list(range(1,n));
    for j in nodes:
        if(([0,j-1],[n-1,j]) not in listp and ([n-1,j],[0,j-1]) not in listp):   
            x = [0,n-1]
            plt.plot(x,[j-1,j])
            listp+=[([0,j-1],[n-1,j])]
            triang+=1
    triang*=2
    if(k%2==1):
        x = [0,(n-1)/2]
        plt.plot(x,[n-1,(2*n-3)/2])
        listp+=[([n-1,n-1],[(n-1)/2,(2*n-3)/2])]
        triang+=1
    print(listp)
    print(triang)   
    print(len(listp))
    plt.axis('equal')
    plt.show()
    return listp


def square3(k,fig=3):
    if(k==2 or k==3):
        listp=square2(k,3)
        return listp
    plt.figure(fig)
    
    if(k==4):
        n=(k-1)//2+1
        nodes=list(range(0,n));
        listp=[]
        
        #decoupage du carré
        for j in nodes:
            
            if((([n-1,j],[0,j]) not in listp) and (n-j!=0) and (([0,j],[n-1,j]) not in listp)):
                x = [n-1,0]
                plt.plot(x,[j,j])
                listp+=[([n-1,j],[0,j])]
                
            if(([0,0],[0,j]) not in listp  and (j!=0) and (([0,j],[0,0]) not in listp)):
                x = [0,0]
                plt.plot(x,[0,j])
                #if([0,0] not in listp):
                listp+=[([0,0],[0,j])]
                
            if(([0,0],[n-1,0]) not in listp  and (n-1!=0) and (([n-1,0],[0,0]) not in listp )):   
                x = [0,n-1]
                plt.plot(x,[0,0])
                #if([n-1,0] not in listp):
                listp+=[([0,0],[n-1,0])]
                
            if(([n-1,0],[n-1,j]) not in listp  and (j!=0) and (([n-1,j],[n-1,0]) not in listp)):
                x = [n-1,n-1]
                plt.plot(x,[0,j])
                listp+=[([n-1,0],[n-1,j])]
        triang=0
        x = [0,j]
        j=1
        plt.plot(x,[j-1,j])
        listp+=[([0,j-1],[j,j])]
        triang+=1
        x = [j,0]
        plt.plot(x,[j-1,j])
        listp+=[([j,j-1],[0,j])]
        triang+=1
    else:
        n=3
        nodes=list(range(0,n));
        listp=[]
        
        #decoupage du carré
        for j in nodes:
            
            if((([n-1,j],[0,j]) not in listp) and (n-j!=0) and (([0,j],[n-1,j]) not in listp)):
                x = [n-1,0]
                plt.plot(x,[j,j])
                listp+=[([n-1,j],[0,j])]
                
            if(([0,0],[0,j]) not in listp  and (j!=0) and (([0,j],[0,0]) not in listp)):
                x = [0,0]
                plt.plot(x,[0,j])
                #if([0,0] not in listp):
                listp+=[([0,0],[0,j])]
                
            if(([0,0],[n-1,0]) not in listp  and (n-1!=0) and (([n-1,0],[0,0]) not in listp )):   
                x = [0,n-1]
                plt.plot(x,[0,0])
                #if([n-1,0] not in listp):
                listp+=[([0,0],[n-1,0])]
                
            if(([n-1,0],[n-1,j]) not in listp  and (j!=0) and (([n-1,j],[n-1,0]) not in listp)):
                x = [n-1,n-1]
                plt.plot(x,[0,j])
                listp+=[([n-1,0],[n-1,j])]
        triang=0
#    nodes=list(range(1,n));
#    for j in nodes:
#        if(([0,j-1],[n-1,j]) not in listp and ([n-1,j],[0,j-1]) not in listp):   
#            x = [0,n-1]
#            plt.plot(x,[j-1,j])
#            listp+=[([0,j-1],[n-1,j])]
#            triang+=1
#    triang*=2
#    if(k%2==1):
#        x = [0,(n-1)/2]
#        plt.plot(x,[n-1,(2*n-3)/2])
#        listp+=[([n-1,n-1],[(n-1)/2,(2*n-3)/2])]
#        triang+=1
    print(listp)
    print(triang)   
    print(len(listp))
    plt.axis('equal')
    plt.show()


square(4)
square2(4)
square3(4)


def regular_polygon(n,r=1,c1=1,c2=1):
    listp=[]
    for i in range(n):
        listp.append((r*cos(2*pi*i/n)+c1,r*sin(2*pi*i/n)+c2))
        
    for i in range (n):
        p1=listp[i]
        if(i!=n-1):
            p2=listp[i+1]
        else:
            p2=listp[0]
     #   plt.plot([p1[0],p2[0]],[p1[1],p2[1]])
    #plt.axis('equal')
    #plt.show()
    return listp
    
def mesh_polygon(n,c1=1,c2=1,dec=False):
    
    polyg_p=regular_polygon(n)
    center=[c1,c2]
    listp=[]
    for i in range (n):
        p1=polyg_p[i]
        if(i!=n-1):
            p2=polyg_p[i+1]
        else:
            p2=polyg_p[0]
        plt.plot([p1[0],p2[0]],[p1[1],p2[1]])
        listp.append((p1,p2))
        plt.plot([p1[0],center[0]],[p1[1],center[1]])
        listp.append((p1,center))
    plt.axis('equal')
    plt.show()
    return listp

mesh_polygon(5,1/2,1)
mesh_polygon(10)
class GeneratePolygon(object):

    """
         Une class qui genere des polygones mailllés.       
    """
    
    def __init__(self):#constructeur de la classe
        return
        
    def regular_polygon(self,n,r=1,c1=1,c2=1):
        listp=[]
        for i in range(n):
            listp.append([r*cos(2*pi*i/n)+c1,r*sin(2*pi*i/n)+c2])
            
#        for i in range (n):
#            p1=listp[i]
#            if(i!=n-1):
#                p2=listp[i+1]
#            else:
#                p2=listp[0]
#            plt.plot([p1[0],p2[0]],[p1[1],p2[1]])
#        plt.axis('equal')
#        plt.show()
        return listp
    
#polygon=GeneratePolygon()
#print(polygon.regular_polygon(10,r=1,c1=4,c2=4))
