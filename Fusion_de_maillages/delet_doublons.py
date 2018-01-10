# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:04:35 2018

enlèves les points doublons dans nodes 

"""

def delet_doublon(nodes3,elems3,informations):
    nodes1 = informations[0]
    elems1 = informations[1]
    nodes2 = informations[2]
    elems2 = informations[3]
    n_nodes_3 = len(nodes3)
    n_elems_3 = len(elems3)


    tab_remplace = []
    for i in range(n_nodes_3):
        tab_remplace.append(-1)
        
    #enleve les doublons
    for i in range(n_nodes_3):
        for j in range(i+1,n_nodes_3):
            if((nodes3[i][1]==nodes3[j][1] and nodes3[i][2]==nodes3[j][2]) or (nodes3[i][1]==nodes3[j][2] and nodes3[i][2]==nodes3[j][1])):
                if(nodes3[i][1]!=-1 and nodes3[i][2]!=-1):    
                    nodes3[j] = [-1,-1,-1,-1]
                    tab_remplace[j] = i +1 #attention -nb_elem_sup
    
    nb_elem_sup = 0
    i = 0               
    while(i < n_nodes_3-nb_elem_sup ):
        if(nodes3[i][0] == -1):
            del nodes3[i]
            nb_elem_sup = nb_elem_sup +1
            for j in range(n_nodes_3):
                if(tab_remplace[j]>i):
                   tab_remplace[j] = tab_remplace[j] -1 
        
        else:
            i = i+1
    
            
    for i in range(n_elems_3):
        for j in range(3):
            if(tab_remplace[elems3[i][j+1]-1]!=-1): #attention tab_remplace[elems3[i][j+1]]-1+1
                elems3[i][j+1] = tab_remplace[elems3[i][j+1]-1] #attention + 1 - 1
            
            
    return nodes3,elems3
    