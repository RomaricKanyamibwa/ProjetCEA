# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:51:05 2018

@author: NightSlayer
"""

from dessine_python import dessine_python
from matplotlib import pyplot as plt
#plt.plot([0,0],'o')
#plt.plot([1,0],'o')
#plt.plot([0,1],'o')

L=[[1,1,2,3]]
P=[[1,0,0],[2,0,1],[3,1,0]]
dessine_python(P,L)

x=0.5
y=-1
plt.plot(x,y,'o')

plt.figure(2)

L=[[1,1,2,3]]
P=[[1,0,0],[2,0,1],[3,1,0]]
dessine_python(P,L)

L=[[1,1,2,3]]
P=[[1,0,0],[2,0,1],[3,x,y]]
dessine_python(P,L)

x=0.5
y=-1
plt.plot(x,y,'o')

plt.figure(3)

L=[[1,1,2,3]]
P=[[1,0,0],[2,0,1],[3,1,0]]
dessine_python(P,L)

L=[[1,1,2,3]]
P=[[1,x,y],[2,0,1],[3,1,0]]
dessine_python(P,L)

x=0.5
y=-1
plt.plot(x,y,'o')

plt.figure(4)

L=[[1,1,2,3]]
P=[[1,0,0],[2,0,1],[3,1,0]]
dessine_python(P,L)

L=[[1,1,2,3]]
P=[[1,0,0],[2,x,y],[3,1,0]]
dessine_python(P,L)

x=0.5
y=-1
plt.plot(x,y,'o')