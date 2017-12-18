"""Voisin des triangles """
#from random import randrange

#import numpy as np

elem3 = [[1,2,7,3],
	[2,4,5,6],
	[3,3,8,9],
	[4,4,8,9],
    [5,7,5,2],
    [6,7,4,2]]


def list_neighbors(triangles):
    """Fonction de  construction de dictionaire de voisin
    Entree:
    -triangles: une liste de n triangles avec leurs sommets
    Sortie:
    -num_triangles
    -d:dictionaire de voisins
    """
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
    #print(d)
    num_triangles=len(triangles)
    return num_triangles,d
#print(len(d))
n,d=list_neighbors(elem3)	
#n1 = input("De quel triangle souhaitez-vous connaître ses voisins ? Je veux connaître ceux du triangle numéro :")

def neighbours(elem,dx):
    """Fonction qui retourne la liste des voisins de triangles
    Arguments:
    -elem3: liste des triangles
    -dx: dictionaire contenant les voisins (on utilise la fonction list_neighbors)
    Sortie;
    -a:liste des voisind de triangles
    
    """
#	cette fonction est pour le maillage conforme
    a = [[]]*(len(elem)+1)
#    print(a)
#    for i in range(1,len(elem)) :
#        a[i] = [i]
    for x in dx.values():
        #print(x)
        if(len(x)==2):
#            print((x[0]))
            a[x[0]]=a[x[0]]+[x[1]]
#            print(x[1])
            a[x[1]]=a[x[1]]+[x[0]]
#            print(a)
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

a3 = neighbours(elem3,d)
