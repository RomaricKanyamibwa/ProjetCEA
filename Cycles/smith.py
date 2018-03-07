#!/usr/bin/env python3
 
from sympy import *
 
def leftmult2(m, i0, i1, a, b, c, d):
    for j in range(m.cols):
        x, y = m[i0, j], m[i1, j]
        m[i0, j] = a * x + b * y
        m[i1, j] = c * x + d * y
 
def rightmult2(m, j0, j1, a, b, c, d):
    for i in range(m.rows):
        x, y = m[i, j0], m[i, j1]
        m[i, j0] = a * x + c * y
        m[i, j1] = b * x + d * y
 
def smith(m, domain=ZZ):
    m = Matrix(m)
    s = eye(m.rows)
    t = eye(m.cols)
    last_j = -1
    for i in range(m.rows):
        for j in range(last_j+1, m.cols):
            if not m.col(j).is_zero:
                break
        else:
            break
        if m[i,j] == 0:
            for ii in range(m.rows):
                if m[ii,j] != 0:
                    break
            leftmult2(m, i, ii, 0, 1, 1, 0)
            rightmult2(s, i, ii, 0, 1, 1, 0)
        rightmult2(m, j, i, 0, 1, 1, 0)
        leftmult2(t, j, i, 0, 1, 1, 0)
        j = i
        upd = True
        while upd:
            upd = False
            for ii in range(i+1, m.rows):
                if m[ii, j] == 0:
                    continue
                upd = True
                if domain.rem(m[ii, j], m[i, j]) != 0:
                    coef1, coef2, g = domain.gcdex(m[i,j], m[ii, j])
                    coef3 = domain.quo(m[ii, j], g)
                    coef4 = domain.quo(m[i, j], g)
                    leftmult2(m, i, ii, coef1, coef2, -coef3, coef4)
                    rightmult2(s, i, ii, coef4, -coef2, coef3, coef1)
                coef5 = domain.quo(m[ii, j], m[i, j])
                leftmult2(m, i, ii, 1, 0, -coef5, 1)
                rightmult2(s, i, ii, 1, 0, coef5, 1)
            for jj in range(j+1, m.cols):
                if m[i, jj] == 0:
                    continue
                upd = True
                if domain.rem(m[i, jj], m[i, j]) != 0:
                    coef1, coef2, g = domain.gcdex(m[i,j], m[i, jj])
                    coef3 = domain.quo(m[i, jj], g)
                    coef4 = domain.quo(m[i, j], g)
                    rightmult2(m, j, jj, coef1, -coef3, coef2, coef4)
                    leftmult2(t, j, jj, coef4, coef3, -coef2, coef1)
                coef5 = domain.quo(m[i, jj], m[i, j])
                rightmult2(m, j, jj, 1, -coef5, 0, 1)
                leftmult2(t, j, jj, 1, coef5, 0, 1)
        last_j = j
    for i1 in range(min(m.rows, m.cols)):
        for i0 in reversed(range(i1)):
            coef1, coef2, g = domain.gcdex(m[i0, i0], m[i1,i1])
            if g == 0:
                continue
            coef3 = domain.quo(m[i1, i1], g)
            coef4 = domain.quo(m[i0, i0], g)
            leftmult2(m, i0, i1, 1, coef2, coef3, coef2*coef3-1)
            rightmult2(s, i0, i1, 1-coef2*coef3, coef2, coef3, -1)
            rightmult2(m, i0, i1, coef1, 1-coef1*coef4, 1, -coef4)
            leftmult2(t, i0, i1, coef4, 1-coef1*coef4, 1, -coef1)
    return (s, m, t)
 
m = Matrix([
    [1, -1],
    [3, 4],
    [0, 2]
    ])
 
print(smith(Matrix([
    [1, 2, 3],
    [-2, 0, 4],
    ])))
print(smith(Matrix([
    [1, 1, 2],
    [2, 1, 3],
    [3, 1, 4],
    ])))
print(smith(Matrix([
    [12, 0, 0],
    [0, 18, 0],
    [0, 0, 210],
    ])))

        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
A = [   [ 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1],
        [ 0, 1,-1, 0,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 1, 1, 0, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 1, 0, 0, 0,-1, 1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,-1,-1, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1, 0, 0,-1, 1]]
        
print(smith(Matrix(A))