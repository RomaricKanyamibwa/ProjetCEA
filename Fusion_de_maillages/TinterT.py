""" Programm for playing the game skyline """
#from random import randrange

import numpy as np

elem1 = np.array([
			[1,4,7,3],
			[2,4,5,3],
			[3,3,8,6],
			[4,4,8,1]])

elem2 = np.array([
			[1,2,7,3],
			[2,4,5,6],
			[3,3,8,9],
			[4,4,8,9]])
def intersect(L1,L2,p11,p12,p21,p22,s1,s2):
    #retourne les coordonnés des points d'intersection et les points des segments qui s'intersectent
    if(L1[1]==0 and L2[1]==0):
        #print "colinéaire"
        #print("infini")
        return False
    if(L1[0]/float(L1[1])==L2[0]/float(L2[1])): #colinéaire
        #print("colinéaire")
        return False
    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        #segment
        if(x<min(p11[0],p12[0],p21[0],p22[0]) or x>max(p11[0],p12[0],p21[0],p22[0]) or y<min(p11[1],p12[1],p21[1],p22[1]) or y>max(p11[1],p12[1],p21[1],p22[1])):         
         #   print("seg")
            return False
        return x,y,p11[2],p12[2],p21[2],p22[2],s1,s2
    else:
       # print("ne se croise pas")        
        return False
        
        
def intersection(t1,t2,s1,s2):
   p11 = [nodes1[elems1[t1][s1+1]-1][1],nodes1[elems1[t1][s1+1]-1][2],elems1[t1][s1+1]] #coordonées du point et numéro du point
   p12 = [nodes1[elems1[t1][(s1+1)%3+1]-1][1],nodes1[elems1[t1][(s1+1)%3+1]-1][2],elems1[t1][(s1+1)%3+1]]
   p21 = [nodes2[elems2[t2][s2+1]-1][1],nodes2[elems2[t2][s2+1]-1][2],elems2[t2][s2+1]]
   p22 = [nodes2[elems2[t2][(s2+1)%3+1]-1][1],nodes2[elems2[t2][(s2+1)%3+1]-1][2],elems2[t2][(s2+1)%3+1]]
   L1 = line(p11,p12)
   L2 = line(p21,p22)    
   R = intersect(L1,L2,p11,p12,p21,p22,s1,s2)
   return R
                
def intersecte(t1,t2):
    for s1 in range(3): # segments du triangle du maillage 1
        for s2 in range(3):#3): # segments du triangle du maillage 2
            R = intersection(t1,t2,s1,s2)
            if(R):
                return True
            else:
                return False
#***************************************************************************************
def list_neighbors(triangles):
    d = dict()
    for x in triangles:
        x[1:]=sorted(x[1:],key=int)
        #print(x)
        t = (x[1],x[2])
        s = (x[2],x[3])
        r = (x[1],x[3])
        if t not in d.keys() :
            d[t]=[]
        if s not in d.keys() :
            d[s]=[]
        if r not in d.keys() :
            d[r]=[]	
        d[t].append(x[0]) 
        d[s].append(x[0]) 
        d[r].append(x[0]) 
    print(d)
    return d

d1=list_neighbors(elem1)
d2=list_neighbors(elem2)		
#n1 = input("De quel triangle souhaitez-vous connaître ses voisins ? Je veux connaître ceux du triangle numéro :")

def neighbours(elem,dx):
#	cette fonction est pour le maillage conforme
    a = [[]]*(len(elem)+1)
    #print(a)
#    for i in range(1,len(elem)) :
#        a[i] = [i]
    for x in dx.values():
        print(x)
        if(len(x)==2):
            print((x[0]))
            a[x[0]]=a[x[0]]+[x[1]]
            print(x[1])
            a[x[1]]=a[x[1]]+[x[0]]
            print(a)
        elif(len(x)==3):
            a[x[0]]=a[x[0]]+[x[1],x[2]]
            a[x[1]]=a[x[1]]+[x[0],x[2]]
            a[x[2]]=a[x[2]]+[x[1],x[0]]
#        if i in j:
#            tmp=j
#            tmp.remove(i)
#            a[i]+=tmp
    print(a)
    return(a)

#*********************************************************************************************
def TinterT(msh1,msh2,dx):
	len1 = len2 = 0
	for sub_list in msh1 : len1 += 1
#	print("1- number of items: %d" % len1)
	for sub_list in msh2 : len2 += 1
#	print("2- number of items: %d" % len2)
	num_T = []
	new_msh1 = msh1.flatten()
	for k,v in enumerate(new_msh1):
		if (k%len1) == 0:
			num_T.append(v)
#	print(num_T)
#	print(new_msh1)
	new_msh2 = msh2.flatten()
	for k,v in enumerate(new_msh2):
		if (k%len2) == 0:
			num_T.append(v)
	print(num_T)
#	print(new_msh2)
	i = 0
	neighB = []
	fin = True
	while fin:
		print("+ %d:" % num_T[i])
		j = len1
		while j > i and j < len1+len2:
			print("%d" % num_T[j], end=' ')
			# S'il y a intersection entre le triangle 1 du mesh1 et les triangles 1,2,3,4 du mesh2:
			if intersecte(num_T[i],num_T[j]):
				# On ajoute les triangles voisins des triangles 1,2,3,4 du mesh2 à neighB
				neighB.append(neighbours(new_msh2,dx))
				# On parcourt la liste neighB
			while v in neighB:
				# Si un des triangles voisins des triangles 1,2,3,4 du mesh2 ne s'intersecte pas avec le triangle 1 du mesh1:
				if not intersecte(num_T[i],num_T[j]):
					# On retire ce triangle de la liste neighB
					del v
			j += 1
			if j == len1+len2:
				j = i
		print()
		i += 1
		if i >= len1:
			fin = False


# Si le triangle 1 du mesh1 s'intersecte (methode intersect() ?? pas moyen de tester) avec les triangles 1,2,3,4 du mesh2 Alors 
# on check si les triangles voisins (methode neighbors()) des triangles 1,2,3,4 du mesh2 s'intersectent aussi avec le triangle 1 du mesh1

a1 = neighbours(elem1,d1)
a2 = neighbours(elem2,d2)
TinterT(elem1,elem2,d2)
TinterT(elem2,elem1,d1)
