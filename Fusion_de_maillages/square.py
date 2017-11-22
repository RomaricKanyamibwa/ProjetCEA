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


square(3)
square2(3)
square3(4)


class GeneratePolygon(object):

    """
         Une class qui genere des polygones mailllés.       
    """
    
    def __init__(self):#constructeur de la classe
        return
        
        
