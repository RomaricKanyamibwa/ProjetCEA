# -*- coding: utf-8 -*-

from croiseToMaillage import *
from dessine_python import *
import matplotlib.pyplot as plt

#affiche le surmaille des deux maillages sources
plt.figure()
print "En vert le surmaillage des deux triangles sources"
dessine_python(nodes3,elems3,'g') 
plt.show()
plt.figure()
print "En bleu le maillage 2 et en rouge le maillage 1"
dessine_python(nodes1,elems1,'r')   #affiche le maillage M1
dessine_python(nodes2,elems2,'b') #affiche le maillage M2
plt.show()


