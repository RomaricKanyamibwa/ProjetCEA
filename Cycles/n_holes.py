# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Éditeur de Spyder
Ce script temporaire est sauvegardé ici :
/home/sasl/eleves/main/3302938/.spyder2/.temp.py
"""
#node = []
#[[0,0,0],[3,0,0],[3,0,3],[0,0,3],
#        [1,0,1],[2,0,1],[2,0,2],[1,0,2],
#        [1,0,1],[2,0,1],[1,0,3],[2,0,3],
#        [0,3,0],[3,3,0],[3,3,3],[0,3,3],
#        [1,3,1],[2,3,1],[2,3,2],[1,3,2],
#        [1,3,1],[2,3,1],[1,3,3],[2,3,3]]

#elem1 = []

#[[0,8,10],[0,30,10],[4,8,5],[7,10,11],[8,9,5],[7,6,11],[9,1,2],[9,2,11],
#        [12,20,22],[12,22,15],[20,17,16],[18,23,22],[20,21,17],[18,19,23],[21,13,14],[21,14,23],
#        [12,13,14],[12,1,0],[13,14,2],[13,2,1],[15,14,2],[15,2,13],[12,15,3],[12,3,0],
#        [16,17,4],[17,4,5],[17,19,5],[19,6,5],[18,19,7],[19,6,7],[16,18,4],[18,7,4]]


def nb_holes(n):
    node = []
    elem1 = []
    for i in range(0,n):
        node.append([0,0+i*3,0])    #0
        node.append([0,3+i*3,0])    #1
        node.append([3,3+i*3,0])    #2
        node.append([3,0+i*3,0])    #3
        
        node.append([1,1+i*3,0])    #4
        node.append([1,2+i*3,0])    #5
        node.append([2,2+i*3,0])    #6
        node.append([2,1+i*3,0])    #7
            
        node.append([0,1+i*3,0])    #8
        node.append([0,2+i*3,0])
        node.append([3,1+i*3,0])
        node.append([3,2+i*3,0])
        

        node.append([0,0+i*3,3])    #12
        node.append([0,3+i*3,3])    #13
        node.append([3,3+i*3,3])    #14
        node.append([3,0+i*3,3])    #15
        
        node.append([1,1+i*3,3])    #16
        node.append([1,2+i*3,3])
        node.append([2,1+i*3,3])
        node.append([2,2+i*3,3])
        
        node.append([0,1+i*3,3])    #20
        node.append([0,2+i*3,3])
        node.append([3,1+i*3,3])
        node.append([3,2+i*3,3])

        node.append([1,3+i*3,0])    #24
        node.append([2,3+i*3,0])
        node.append([1,0+i*3,0])
        node.append([2,0+i*3,0])

        node.append([1,3+i*3,3])
        node.append([2,3+i*3,3])
        node.append([1,0+i*3,3])    #30
        node.append([2,0+i*3,3])
        
        
        elem1.append([0+i*32,8+i*32,4+i*32])    #1
        elem1.append([0+i*32,26+i*32,4+i*32])   #2
        elem1.append([8+i*32,5+i*32,4+i*32])    #3
        elem1.append([7+i*32,10+i*32,11+i*32])  #4
        elem1.append([8+i*32,9+i*32,5+i*32])    #5
        elem1.append([7+i*32,6+i*32,11+i*32])   #6
        elem1.append([9+i*32,1+i*32,24+i*32])   #7
        elem1.append([9+i*32,24+i*32,5+i*32])   #8
        
        elem1.append([12+i*32,20+i*32,16+i*32]) #9
        
        elem1.append([12+i*32,16+i*32,30+i*32])
        elem1.append([20+i*32,17+i*32,16+i*32])
        
        elem1.append([18+i*32,23+i*32,22+i*32])
        elem1.append([20+i*32,21+i*32,17+i*32])
        elem1.append([18+i*32,19+i*32,23+i*32])
        elem1.append([21+i*32,13+i*32,28+i*32])
        elem1.append([21+i*32,28+i*32,17+i*32])
        elem1.append([12+i*32,20+i*32,8+i*32])  #17
        elem1.append([12+i*32,8+i*32,0+i*32])   #18
        
        #elem1.append([13+i*32,24+i*32,28+i*32])
        #elem1.append([13+i*32,1+i*32,24+i*32])
        
        elem1.append([15+i*32,22+i*32,10+i*32]) #21
        elem1.append([15+i*32,10+i*32,3+i*32])  #22
        
        #elem1.append([12+i*32,30+i*32,26+i*32])#23
        #elem1.append([12+i*32,26+i*32,0+i*32]) #24
        
        elem1.append([16+i*32,17+i*32,4+i*32])
        elem1.append([17+i*32,4+i*32,5+i*32])
        
        elem1.append([17+i*32,19+i*32,5+i*32])
        elem1.append([19+i*32,6+i*32,5+i*32])
        
        elem1.append([18+i*32,19+i*32,7+i*32])
        elem1.append([19+i*32,6+i*32,7+i*32])
        
        elem1.append([16+i*32,18+i*32,4+i*32])
        elem1.append([18+i*32,7+i*32,4+i*32])   #32

        #correction

        elem1.append([4+i*32,7+i*32,26+i*32])   #33
        elem1.append([7+i*32,26+i*32,27+i*32])
        elem1.append([7+i*32,27+i*32,10+i*32])
        elem1.append([3+i*32,10+i*32,27+i*32])
        elem1.append([5+i*32,24+i*32,25+i*32])
        elem1.append([25+i*32,6+i*32,5+i*32])
        elem1.append([2+i*32,6+i*32,25+i*32])
        elem1.append([6+i*32,2+i*32,11+i*32])   #40
        
        
        elem1.append([16+i*32,18+i*32,30+i*32]) #41
        elem1.append([30+i*32,18+i*32,31+i*32])
        elem1.append([31+i*32,18+i*32,22+i*32])
        elem1.append([15+i*32,31+i*32,22+i*32])
        elem1.append([17+i*32,28+i*32,29+i*32])
        elem1.append([29+i*32,19+i*32,17+i*32])
        elem1.append([14+i*32,19+i*32,29+i*32])
        elem1.append([19+i*32,14+i*32,23+i*32]) #48

        elem1.append([9+i*32,21+i*32,20+i*32])  #49
        elem1.append([20+i*32,8+i*32,9+i*32])   #50
        elem1.append([21+i*32,1+i*32,13+i*32])  #51
        elem1.append([9+i*32,21+i*32,1+i*32])   #52

        #elem1.append([28+i*32,29+i*32,25+i*32]) #53
        #elem1.append([28+i*32,24+i*32,25+i*32]) #54
        #elem1.append([29+i*32,2+i*32,14+i*32])  #55
        #elem1.append([29+i*32,25+i*32,2+i*32])  #56
        
        
        elem1.append([11+i*32,23+i*32,22+i*32]) #57
        elem1.append([11+i*32,22+i*32,10+i*32]) #58
        elem1.append([2+i*32,14+i*32,23+i*32])   #59
        elem1.append([23+i*32,11+i*32,2+i*32])  #60
        
        #elem1.append([30+i*32,31+i*32,27+i*32]) #61
        #elem1.append([30+i*32,26+i*32,27+i*32]) #62
        #elem1.append([31+i*32,15+i*32,3+i*32])  #63
        #elem1.append([31+i*32,27+i*32,3+i*32])  #64
        

        if(i == n-1):
            elem1.append([13+i*32,24+i*32,28+i*32])
            elem1.append([13+i*32,1+i*32,24+i*32])
            elem1.append([28+i*32,29+i*32,25+i*32]) #53
            elem1.append([28+i*32,24+i*32,25+i*32]) #54
            elem1.append([29+i*32,2+i*32,14+i*32])  #55
            elem1.append([29+i*32,25+i*32,2+i*32])  #56
        if(i == 0):
            elem1.append([12+i*32,30+i*32,26+i*32])#23
            elem1.append([12+i*32,26+i*32,0+i*32]) #24
            elem1.append([30+i*32,31+i*32,27+i*32]) #61
            elem1.append([30+i*32,26+i*32,27+i*32]) #62
            elem1.append([31+i*32,15+i*32,3+i*32])  #63
            elem1.append([31+i*32,27+i*32,3+i*32])  #64
        
    return(node,elem1)

#(node,elem1)=nb_holes(1)
#draw_cycle([], node, elem1, [])

