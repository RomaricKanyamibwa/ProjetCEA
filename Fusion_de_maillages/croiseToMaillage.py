# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:24:11 2018

@author: colette
"""
from intersection import *
from triangles_inclus import *
from dessine_python import *
from barycentre import *
from chargement_des_donnees import *
from tinter import *


nodes3 = []
elems3 = []
n_nodes_3 = 0
n_elems_3 = 0
info_m3 = [nodes3,elems3]


def coordo(triangle, sommet, information_maillage_i): #triangle correspond a l indice et non au numer du triangle 
    '''donne les coordonnees du sommet du triangle du maillage i'''
    nodes = information_maillage_i[0]
    elems = information_maillage_i[1]
      
    x = nodes[elems[triangle][sommet+1]-1][1]
    y = nodes[elems[triangle][sommet+1]-1][2]
    return(x,y)
    
    
            
def creation_maillage3_1_ptinter(triangle1,triangle2,informations,info_m3,R,n_nodes_3,n_elems_3):
    '''remplis nodes3 et elems 3 quand deus triangle ne se croisent qu'en un seul points '''
    #print "intersection 1"
    nodes3 = info_m3[0] 
    elems3 = info_m3[1]
    n_init = n_nodes_3
    
    
    for so2 in range(3): # les sommets du trinagle 2
        x2 = coordo(triangle2, so2, info_m2)[0]
        y2 = coordo(triangle2, so2, info_m2)[1]
        if((x2==coordo(triangle1,0,info_m1)[0] and y2==coordo(triangle1,0,info_m1)[1]) or (x2==coordo(triangle1,1,info_m1)[0] and y2==coordo(triangle1,1,info_m1)[1]) or (x2==coordo(triangle1,2,info_m1)[0] and y2==coordo(triangle1,2,info_m1)[1])):
            #point_inter_triangle(x2,y2,triangle1) and not point_inter_strict_triangle(x2,y2,triangle1)): #dit sile point (x2,y2) (appartenant au triangle 2) est inclus dans le triangles1        
            n_nodes_3 = n_nodes_3 + 1                
            nodes3.append([n_nodes_3,coordo(triangle2, so2, info_m2)[0],coordo(triangle2, so2, info_m2)[1],0])

        #print nodes3,elems3
    n_nodes_3 = n_nodes_3 + 1  
    nodes3.append([n_nodes_3,R[0],R[1],0])
    if(n_nodes_3-n_init==2):
        for so1 in range(3): # les sommets du trinagle 1
            x1 = coordo(triangle1, so1, info_m1)[0]
            y1 = coordo(triangle1, so1, info_m1)[1]
            if(point_inter_strict_triangle_m2(x1,y1,triangle2)):
                n_nodes_3 = n_nodes_3 + 1                
                nodes3.append([n_nodes_3,x1,y1,0])
        
        
    
    n_elems_3 = n_elems_3 + 1
    
    elems3.append([n_elems_3,n_nodes_3,n_nodes_3-1, n_nodes_3-2])
    
    return (nodes3,elems3,n_nodes_3,n_elems_3)

def creation_maillage3_ptinter(triangle1,triangle2,informations,info_m3,pt_intersection,n_nodes_3,n_elems_3):
    '''remplis nodes3 et elems 3 quand deus triangle ne se croisent en plusieurs points '''
    #print "intersection multiple"
    #print pt_intersection
    nodes3 = info_m3[0] 
    elems3 = info_m3[1]
    
    nb_pt_intersection = len(pt_intersection)
    (xb,yb) = barycentre(pt_inter,nb_pt_intersection)


    n_nodes_3 = n_nodes_3 + 1
    n_bary = n_nodes_3
    nodes3.append([n_nodes_3, xb,yb,0])
    
    for i in range(2): #trinagle 0, triangle 1
        for j in range(nb_pt_inter):
            for k in range(j,nb_pt_intersection):
                if(len(pt_intersection[j])>8):                
                    if(pt_intersection[j][6+i+2]==pt_intersection[k][6+i] and (pt_intersection[j][0]!=pt_intersection[k][0] or pt_intersection[j][1]!=pt_intersection[k][1])): #un segment du triangle i est coupe par 2 segments de lautre triangle     
                        n_nodes_3 = n_nodes_3 + 1
                        nodes3.append([n_nodes_3, pt_intersection[k][0],pt_intersection[k][1],0])                            
                        n_nodes_3 = n_nodes_3 + 1
                        nodes3.append([n_nodes_3, pt_intersection[j][0],pt_intersection[j][1],0])
                        n_elems_3 = n_elems_3 + 1
                        elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])
                if(len(pt_intersection[k])>8):                
                    if(pt_intersection[j][6+i]==pt_intersection[k][6+i+2] and (pt_intersection[j][0]!=pt_intersection[k][0] or pt_intersection[j][1]!=pt_intersection[k][1])): #un segment du triangle i est coupe par 2 segments de lautre triangle
                        n_nodes_3 = n_nodes_3 + 1
                        nodes3.append([n_nodes_3, pt_intersection[k][0],pt_intersection[k][1],0])                            
                        n_nodes_3 = n_nodes_3 + 1
                        nodes3.append([n_nodes_3, pt_intersection[j][0],pt_intersection[j][1],0])
                        n_elems_3 = n_elems_3 + 1
                        elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])
                
                
                if(pt_intersection[j][6+i]==pt_intersection[k][6+i] and (pt_intersection[j][0]!=pt_intersection[k][0] or pt_intersection[j][1]!=pt_intersection[k][1])): #un segment du triangle i est coupe par 2 segments de lautre triangle
                    n_nodes_3 = n_nodes_3 + 1
                    nodes3.append([n_nodes_3, pt_intersection[k][0],pt_intersection[k][1],0])                            
                    n_nodes_3 = n_nodes_3 + 1
                    nodes3.append([n_nodes_3, pt_intersection[j][0],pt_intersection[j][1],0])
                    n_elems_3 = n_elems_3 + 1
                    elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])
                    
    #les sommets qui sont dans le triangle
    for so2 in range(3):
        x2 = coordo(triangle2, so2, info_m2)[0]
        y2 = coordo(triangle2, so2, info_m2)[1]
        if(point_inter_triangle(x2,y2,triangle1)): #dit sile point (x2,y2) (appartenant au triangle 2) est inclus dans le triangles1        
            #print "POINT INTER !!!! "
            #print x2,y2 
            n_nodes_3 = n_nodes_3 + 1
            n_x2_y2 = n_nodes_3
            nodes3.append([n_nodes_3, x2,y2,0]) #################ICI DE LA REDONDANCE            
            for i in range(nb_pt_inter):
                if(pt_intersection[i][4]== elems2[triangle2][so2+1] or pt_intersection[i][5]== elems2[triangle2][so2+1]): 
                    n_nodes_3 = n_nodes_3 + 1
                    nodes3.append([n_nodes_3, pt_intersection[i][0],pt_intersection[i][1],0])
                    n_elems_3 = n_elems_3 + 1
                    elems3.append([n_elems_3, n_bary, n_nodes_3,n_x2_y2])
                    
    for so1 in range(3): # les sommets du trinagle 1
        x1 = coordo(triangle1, so1, info_m1)[0]
        y1 = coordo(triangle1, so1, info_m1)[1]
        if(point_inter_strict_triangle_m2(x1,y1,triangle2)): #dit sile point (x1,y1) (appartenant au triangle 1) est inclus dans le triangles2                   
            n_nodes_3 = n_nodes_3 + 1      
            n_x1_y1 = n_nodes_3
            nodes3.append([n_nodes_3,coordo(triangle1, so1, info_m1)[0],coordo(triangle1, so1, info_m1)[1],0])
            for i in range(nb_pt_inter):
                if(pt_intersection[i][2]== elems1[triangle1][so1+1] or pt_intersection[i][3]== elems1[triangle1][so1+1]):                    
                    n_nodes_3 = n_nodes_3 + 1
                    nodes3.append([n_nodes_3, pt_intersection[i][0],pt_intersection[i][1],0])
                    n_elems_3 = n_elems_3 + 1
                    elems3.append([n_elems_3, n_bary, n_nodes_3,n_x1_y1])

                    
    
    
    return (nodes3,elems3,n_nodes_3,n_elems_3)

def creation_maillage3_2_ptinter(triangle1,triangle2,informations,info_m3,pt_intersection,n_nodes_3,n_elems_3):
    '''remplis nodes3 et elems 3 quand deus triangle ne se croisent en 2 points '''
    #print "2intersections"
    nodes3 = info_m3[0] 
    elems3 = info_m3[1]
    
    pt_inter_triangle = []
    
    if(pt_intersection[0][6]==pt_intersection[1][6]): #si le triangle 2 coupe deux fois le meme segment du triangle 1
        #print "2 fois meme segment"        
        for so in range(3):   
            (x2,y2) = coordo(triangle2, so, info_m2)
            if(point_inter_triangle(x2,y2,triangle1)):
                pt_inter_triangle.append([x2,y2,elems2[triangle2][so+1]]) #x,y, et numero de sommet
        if(len(pt_inter_triangle)==1):
            #print"1 point inter"
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[0][0],pt_intersection[0][1],0])                            
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[1][0],pt_intersection[1][1],0])
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_inter_triangle[0][0],pt_inter_triangle[0][1],0])
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_nodes_3-2,n_nodes_3-1,n_nodes_3])
        else:
            #print "2point inter"
            nb_pt_intersection = 4
            pt_intersection.append([pt_inter_triangle[0][0],pt_inter_triangle[0][1]])
            pt_intersection.append([pt_inter_triangle[1][0],pt_inter_triangle[1][1]])
            (xb,yb) = barycentre(pt_intersection,nb_pt_intersection)
            n_nodes_3 = n_nodes_3 + 1
            n_bary = n_nodes_3
            nodes3.append([n_nodes_3, xb,yb,0])
            n_nodes_3 = n_nodes_3 + 1
            n_pt_intersect = n_nodes_3
            nodes3.append([n_nodes_3, pt_intersection[0][0],pt_intersection[0][1],0])                            
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[1][0],pt_intersection[1][1],0])
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])

            n_nodes_3 = n_nodes_3 + 1
            n_sommet_1 = n_nodes_3
            nodes3.append([n_nodes_3, pt_inter_triangle[0][0],pt_inter_triangle[0][1],0]) #sommet 1
            n_nodes_3 = n_nodes_3 + 1
            n_sommet_2 = n_nodes_3
            nodes3.append([n_nodes_3, pt_inter_triangle[1][0],pt_inter_triangle[1][1],0])  #sommet 2       
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_bary, n_nodes_3,n_nodes_3-1])
            
            #print "POINT INTERSECTION"
            #print pt_intersection     
            #print pt_inter_triangle
            
            for i in range(2): #pt intersection
                for j in range(2): #pt inter triangle
                    if(pt_intersection[i][4]-1 == pt_inter_triangle[j][2]-1 or pt_intersection[i][5]-1 == pt_inter_triangle[j][2]-1):
                        #print 'tada' 
                        #print pt_inter_triangle[j][2]
                        #print pt_inter_triangle
                        n_elems_3 = n_elems_3 + 1
                        elems3.append([n_elems_3, n_bary, n_sommet_1+j,n_pt_intersect+i])

    else: # il y a deux segments differrents qui sont coupes
        for so in range(3):   
            (x2,y2) = coordo(triangle2, so, info_m2)
            if(point_inter_strict_triangle(x2,y2,triangle1)):
                pt_inter_triangle.append([x2,y2,elems2[triangle2][so+1]]) #x,y, et numero de sommet
        if(len(pt_inter_triangle)==1):
            #un seul point a l interieur
            n_nodes_3 = n_nodes_3 + 1
            n_intersect_1 = n_nodes_3
            nodes3.append([n_nodes_3, pt_intersection[0][0],pt_intersection[0][1],0])                            
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[1][0],pt_intersection[1][1],0])
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_inter_triangle[0][0],pt_inter_triangle[0][1],0])
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_nodes_3-2,n_nodes_3-1,n_nodes_3])
            
            for so in range(3):   
                (x1,y1) = coordo(triangle1, so, info_m1)
                if(point_inter_triangle_m2(x1,y1,triangle2)):
                    #print "X1,Y1"
                    #print x1,y1
                    pt_inter_triangle.append([x1,y1,elems1[triangle1][so+1]]) #x,y, et numero de sommet
                    #print pt_inter_triangle
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_inter_triangle[1][0],pt_inter_triangle[1][1],0]) #sommet 1
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_intersect_1,n_intersect_1+1,n_nodes_3])
            
        if(len(pt_inter_triangle)==0):
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[0][0],pt_intersection[0][1],0])                            
            n_nodes_3 = n_nodes_3 + 1
            nodes3.append([n_nodes_3, pt_intersection[1][0],pt_intersection[1][1],0])
            
            for so in range(3):   
                (x1,y1) = coordo(triangle1, so, info_m1)
                #print "x1,y1"
                #print x1,y1
                if(point_inter_triangle_m2(x1,y1,triangle2)):
                    #print"BAH SI TAS FAIT TTRUE"
                    #print "X1,Y1"
                    #print x1,y1
                    pt_inter_triangle.append([x1,y1,elems1[triangle1][so+1]]) #x,y, et numero de sommet
                    #print pt_inter_triangle
            n_nodes_3 = n_nodes_3 + 1
            #print"pt inter"
            #print pt_inter_triangle, triangle1,triangle2
            nodes3.append([n_nodes_3, pt_inter_triangle[0][0],pt_inter_triangle[0][1],0]) #sommet 1
            n_elems_3 = n_elems_3 + 1
            elems3.append([n_elems_3, n_nodes_3-2,n_nodes_3-1,n_nodes_3])
        

    return (nodes3,elems3,n_nodes_3,n_elems_3)

#croise = [[0]]# avec les indice et non les numeros de triangle
#[[0, 2, 4, 5], [1, 4, 3, 2], [4, 3, 2, 5], [3], [4, 3, 5], [5]]
#[[3], [1, 0], [3, 1, 0], [3, 0], [0, 2, 3, 1], [2, 0, 3, 1]]

#croise = [[],[],[0],[]]
for triangle1 in range(len(croise)): #indice non num triangle
    for t2 in range(len(croise[triangle1])):
        triangle2 = croise[triangle1][t2]
        nb_pt_inter = 0
        pt_inter = []
        for s1 in range(3): # segments du triangle du maillage 1
            for s2 in range(3):#3): # segments du triangle du maillage 2
                go = True                
                #on cherche le point d intersection de deux segments l un d un triangle t1 et l'autre d'un t2
                R = intersection(triangle1,triangle2,s1,s2,informations)
                #print R
                if(R):
                    #print "il y a R"
                    x2 = R[0]
                    y2 = R[1]
                    #print "x2,y2"
                    #print x2,y2, s1,s2
                    #if((x2==coordo(triangle1,0,info_m1)[0] and y2==coordo(triangle1,0,info_m1)[1]) or (x2==coordo(triangle1,1,info_m1)[0] and y2==coordo(triangle1,1,info_m1)[1]) or (x2==coordo(triangle1,2,info_m1)[0] and y2==coordo(triangle1,2,info_m1)[1])):
                        #print coordo(triangle1,0,info_m1), coordo(triangle1,1,info_m1), coordo(triangle1,2,info_m1)
                        
                        #go = False
                        #print "flase làa"
                        #if((x2==coordo(triangle2,0,info_m2)[0] and y2==coordo(triangle2,0,info_m2)[1]) or (x2==coordo(triangle2,1,info_m2)[0] and y2==coordo(triangle2,1,info_m2)[1]) or (x2==coordo(triangle2,2,info_m2)[0] and y2==coordo(triangle2,2,info_m2)[1])):
                            #go = True
                    for i in range(len(pt_inter)):
                        if(pt_inter[i][0]==R[0] and pt_inter[i][1]==R[1]): #pt deja mis
                            go = False
                            pt_inter[i].append(R[6])
                            pt_inter[i].append(R[7])
                if(R and go):
                    nb_pt_inter = nb_pt_inter + 1
                    pt_inter.append(R)
        #print(nb_pt_inter, triangle1,triangle2)
        #print(pt_inter)
        
        
        if(nb_pt_inter == 1):
            #print "1 seul point d'intersection !!!!!"
            (nodes3,elems3,n_nodes_3,n_elems_3) = creation_maillage3_1_ptinter(triangle1,triangle2,informations,info_m3,pt_inter[0],n_nodes_3,n_elems_3)
            #print elems3,nodes3
            
        if(nb_pt_inter == 2):
            (nodes3,elems3,n_nodes_3,n_elems_3) = creation_maillage3_2_ptinter(triangle1,triangle2,informations,info_m3,pt_inter,n_nodes_3,n_elems_3)
        if(nb_pt_inter > 2):
            #print "il y a"
            #print nb_pt_inter
            (nodes3,elems3,n_nodes_3,n_elems_3) = creation_maillage3_ptinter(triangle1,triangle2,informations,info_m3,pt_inter,n_nodes_3,n_elems_3)
            
