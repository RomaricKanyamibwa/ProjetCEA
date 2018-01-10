import numpy as np
from neighbors import neighbours

def mshToPython_triangle(nom_fichier):
    f1 = open(nom_fichier)

    li = f1.readline().split() 

    while(li[0]!='$Nodes'  and li[0]!='$Nodes\n'):  
        li = f1.readline().split() # '$Nodes\n'

    n_nodes = int(f1.readline())

    nodes = np.fromfile(f1,count=n_nodes*4, sep=" ").reshape((n_nodes,4)) #tableau des noeuds

    f1.readline() # '$EndNodes\n'
    f1.readline() # '$Elements\n'
    n_elems = int(f1.readline()) # '2\n'

    elems = []

    for line in f1:
        ligne = line.split(' ')
        if(ligne[0]!='$EndElements\r\n' and ligne[0]!='$EndElements\n'):
            ligne = map(int, ligne)
            if(ligne[1]==2):
                del ligne[1]
                for i in range(ligne[1]+1):
                    del ligne[1]
                elems.append(ligne)
        
    f1.close()
    n_elems = len(elems)
    return (nodes, elems, n_nodes, n_elems)    
   

(nodes1, elems1, n_nodes_1, n_elems_1) = mshToPython_triangle("Fichier_MSH/maillage1.msh")
(nodes2, elems2, n_nodes_2, n_elems_2) = mshToPython_triangle("Fichier_MSH/maillage2.msh")

voisin1 = [[2,3],[1,7],[1,4,5],[3],[6,3],[7,5],[2,8,6],[7]]
voisin2 = [[2],[1,3,5],[2,4],[3,7],[6,2],[5,7],[6,8,4],[7]]
neighbours(voisin1)

##POUR GERER L INTERSECTION
def intersect(L1,L2,p11,p12,p21,p22,s1,s2):
    #retourne les coordonnes des points d intersection et les points des segments qui s intersectent   
    if(L1[1]==0 and L2[1]==0):
        #print "colineaire"
        #print "infini"
        return False
    if(L1[0]/float(L1[1])==L2[0]/float(L2[1])): #colineaire
        #print "colineaire"
        return False
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        #segment
        if(x<min(p11[0],p12[0]) or x<min(p21[0],p22[0]) or x>max(p11[0],p12[0]) or x>max(p21[0],p22[0]) or y<min(p11[1],p12[1]) or y<min(p21[1],p22[1]) or y>max(p11[1],p12[1]) or y>max(p21[1],p22[1])):         
            #print "seg"
            return False
        if((p11[0]==p21[0] and p11[1]==p21[1]) or (p12[0]==p21[0] and p12[1]==p21[1]) or (p11[0]==p22[0] and p11[1]==p22[1]) or (p12[0]==p22[0] and p12[1]==p22[1])):
            #print "sommet qui se croisent"
            return False
        return x,y,p11[2],p12[2],p21[2],p22[2],s1,s2
    else:
        #print "ne se croise pas"        
        return False
        
def line(p1,p2):
    A = (p1[1]-p2[1])
    B = (p2[0]-p1[0])
    C = (p1[0]*p2[1]-p2[0]*p1[1])
    return A,B,-C
    
def intersection(t1,t2,s1,s2):
   p11 = [nodes1[elems1[t1][s1+1]-1][1],nodes1[elems1[t1][s1+1]-1][2],elems1[t1][s1+1]] #coordonees du point et numero du point
   p12 = [nodes1[elems1[t1][(s1+1)%3+1]-1][1],nodes1[elems1[t1][(s1+1)%3+1]-1][2],elems1[t1][(s1+1)%3+1]]
   p21 = [nodes2[elems2[t2][s2+1]-1][1],nodes2[elems2[t2][s2+1]-1][2],elems2[t2][s2+1]]
   p22 = [nodes2[elems2[t2][(s2+1)%3+1]-1][1],nodes2[elems2[t2][(s2+1)%3+1]-1][2],elems2[t2][(s2+1)%3+1]]
   L1 = line(p11,p12)
   L2 = line(p21,p22)    
   #print(p11, p12,p21,p22)
   R = intersect(L1,L2,p11,p12,p21,p22,s1,s2)
   return R
                
def intersecte(t1,t2):
    R = False
    for s1 in range(3): # segments du triangle du maillage 1
        for s2 in range(3): # segments du triangle du maillage 2
            #print(s1,s2)
            R = intersection(t1,t2,s1,s2)
            if(R):
                return True
    return False
                
                
    
          

def TinterT(msh1,msh2, voisin_m1, voisin_m2):
    len1 = len(msh1)
    len2 = len(msh2)
    intersect = [[] for i in range(len1)] #mailage 1    
    
    t1 = 0
    #on cherche un triangle dans le maillage 2 qui intersecte t1
    i = 0    
    while(intersecte(t1,i) == False):
        i = i+1
    t2 = i
    intersect[t1].append(t2)
            
         
    aParcourir = []
    #on parcours 3 voisins de voisins
    ni = len(voisin_m2[t2])
    for i in range(ni):
        aParcourir.append(voisin_m2[t2][i])
    
    #print(aParcourir)
    n_1 = 0
    for k in range(2):
        n = len(aParcourir) ##attention pas du debut dou le n_1
        for i in range(n_1,n):
            nj = len(voisin_m2[aParcourir[i]-1])
            for j in range(nj):
                if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                    aParcourir.append(voisin_m2[aParcourir[i]-1][j]) #attention n ou n-1
        n_1 = n
   
    #dans les voisins a parcourir on regarde ceux qui coupent t1
    for i in range(len(aParcourir)):
        if(intersecte(t1,aParcourir[i]-1)):
            if(aParcourir[i]-1 not in intersect[t1]):
                t2 = aParcourir[i]-1
                intersect[t1].append(t2)
            
   
    triangles1_ordres_parcours = [2,3,4,5,6,7,1] #########attention a faire
          
    for l in range(len(triangles1_ordres_parcours)):  #choisir t1 attention
        ####################################trouver t2
        t1 = triangles1_ordres_parcours[l]
        nontrouve = True
        aParcourir = []

        ni = len(voisin_m2[t2])
        for i in range(ni):
            aParcourir.append(voisin_m2[t2][i])
        n_1 = 0
        #print(aParcourir)

        for i in range(len(aParcourir)):
            if(intersecte(t1,aParcourir[i]-1)):
                t2 = aParcourir[i]-1
                intersect[t1].append(t2)
                nontrouve = False
        
        

        while nontrouve:
            print("non trouve")
            print (t1,t2)
            n = len(aParcourir)
            for i in range(n_1,n):
                nj = len(voisin_m2[aParcourir[i]-1])
                for j in range(nj):
                    if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                        aParcourir.append(voisin_m2[aParcourir[i]-1][j])
                        if(intersecte(t1,voisin_m2[aParcourir[i]-1][j]-1)):
                            t2 = voisin_m2[aParcourir[i]-1][j]-1
                            intersect[t1].append(t2)
                            nontrouve = False                    
                n_1 = n
            print (aParcourir)
               
        ######################################
        aParcourir = []
        print(t1,t2)
        #on parcours 3 voisins de voisins
        ni = len(voisin_m2[t2])
        for i in range(ni):
            aParcourir.append(voisin_m2[t2][i])
        #print(aParcourir)
        n_1 = 0
        for k in range(2):
            n = len(aParcourir) ##attention pas du debut dou le n_1
            for i in range(n_1,n):
                nj = len(voisin_m2[aParcourir[i]-1])
                for j in range(nj):
                    if(voisin_m2[aParcourir[i]-1][j] not in aParcourir):
                        aParcourir.append(voisin_m2[aParcourir[i]-1][j]) #attention n ou n-1
            n_1 = n
   
        #dans les voisins a parcourir on regarde ceux qui coupent t1
        for i in range(len(aParcourir)):
            if(intersecte(t1,aParcourir[i]-1)):
                if(aParcourir[i]-1 not in intersect[t1]):
                    t2 = aParcourir[i]-1
                    intersect[t1].append(t2)  
        print (aParcourir)
        print(intersect)
    return intersect

croise = TinterT(elems1,elems2, voisin1, voisin2)

def superposition(node1,node2,elems1,elems2, voisin1, voisin2, intersecte):
    nodes3 = []
    elems3 = []
    n_nodes_3 = len(node1+node2)
    n_elems_3 = 0
    for i in range(n_nodes_1): #recopie les nodes de 1, attention ne prend pas en compte les noeuds different de 2
        nodes3.append(nodes1[i])
    for i in range(n_nodes_2): #recopie les nodes de 1, attention ne prend pas en compte les noeuds different de 2
        nodes3.append(nodes2[i])
    for t1 in range(len(intersecte)):
        for t2 in intersecte[t1]:
            for s1 in range(3): # segments du triangle du maillage 1
                for s2 in range(3):#3): # segments du triangle du maillage 2
                #on cherche le point d'intersection de deux segments l'un d'un triangle t1 et l'autre d'un t2
                    R = intersection(t1,t2,s1,s2)
                    if(R):
                        pt_intersection=R
            nodes3.append([0, pt_intersection[0],pt_intersection[1],0])
            n_nodes_3 = n_nodes_3 + 1
    print("r")
    print(pt_intersection)
            
            #########attention point particulier pour 1 et 2
superposition(nodes1,nodes2,elems1,elems2, voisin1, voisin2, croise)