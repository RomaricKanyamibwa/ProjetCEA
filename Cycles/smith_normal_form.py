from sympy import *

# Input from assignment:
# Matrix of coefficients
matrix = Matrix([
    [7, -5, -2, -4],
    [-3, 2, 1, 2],
    [2, -1, -1, -2],
    [-1, 0, 1, 2],
    [0, -1, 1, 2]
])

# Vector of free members
b = [0, 0, 0, 0, 0]

def myfunction():
    myfunction.counter += 1
myfunction.counter = 0

def ppr(matr, left, right):
    myfunction()
    #pprint([left, matr, right])
    print(myfunction.counter,":-----------------------------------------------")
    return

# Moves least element in south-western block, that starts at position [s, s] into start position
def move_least_to_start(matr: Matrix, left: Matrix, right: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))

    pos = [s, s]
    num = abs(matr[s, s])
    for i in range(s, rows):
        for j in range(s, cols):
            if matr[i, j] != 0 and (num == 0 or abs(matr[i, j]) < num):
                pos = [i, j]
                num = abs(matr[i, j])

    if pos[0] != s:
        matr.row_swap(s, pos[0])
        left.row_swap(s, pos[0])

    if pos[1] != s:
        matr.col_swap(s, pos[1])
        right.col_swap(s, pos[1])

    if matr[s, s] < 0:
        matr.row_op(s, lambda val, col: -val)
        left.row_op(s, lambda val, col: -val)


# Modifies edging by standard operations in order to make it zero, should be followed by null_edging()
def modify_edging(matr: Matrix, left: Matrix, right: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))

    for i in range(s + 1, rows):
        if matr[i, s] != 0:
            q = matr[i, s] // matr[s, s]
            matr.row_op(i, lambda val, col: val - q * matr[s, col])
            left.row_op(i, lambda val, col: val - q * left[s, col])

    for i in range(s + 1, cols):
        if matr[s, i] != 0:
            q = matr[s, i] // matr[s, s]
            matr.col_op(i, lambda val, row: val - q * matr[row, s])
            right.col_op(i, lambda val, row: val - q * right[row, s])


# Moves least element in edging, that starts at position [s, s] into start position
def move_le_to_start(matr: Matrix, left: Matrix, right: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))
    pos = [s, s]
    num = abs(matr[s, s])

    for i in range(s + 1, rows):
        if matr[i, s] != 0 and abs(matr[i, s]) < num:
            pos = [i, s]
            num = abs(matr[i, s])
    for j in range(s + 1, cols):
        if matr[s, j] != 0 and abs(matr[s, j]) < num:
            pos = [s, j]
            num = abs(matr[s, j])

    if pos[1] == s and pos[0] > s:
        matr.row_swap(s, pos[0])
        left.row_swap(s, pos[0])
    elif pos[0] == s and pos[1] > s:
        matr.col_swap(s, pos[1])
        right.col_swap(s, pos[1])


# Makes edging, that starts at pos [s, s] zero, ensures south-western block does not divide element at pos [s, s]
def null_edging(matr: Matrix, left: Matrix, right: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))

    while not (matr[s + 1: rows, s].is_zero and matr[s, s + 1: cols].is_zero):
        move_le_to_start(matr, left, right, s)
        modify_edging(matr, left, right, s)

    if matr[s, s] < 0:
        matr.row_op(s, lambda val, col: -val)
        left.row_op(s, lambda val, col: -val)

    ensure_nb_divides(matr, left, right, s)


# Ensures south-western block does not divide element at pos [s, s]
def ensure_nb_divides(matr: Matrix, left: Matrix, right: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))
    pos = [s, s]
    num = matr[s, s]

    for i in range(s + 1, rows):
        for j in range(s + 1, cols):
            if matr[i, j] % matr[s, s] != 0 and matr[i, j] % matr[s, s] < num:
                pos = [i, j]
                num = matr[i, j] % matr[s, s]

    if pos != [s, s]:
        matr.row_op(s, lambda val, col: val + matr[pos[0], col])
        left.row_op(s, lambda val, col: val + left[pos[0], col])

        q = matr[s, pos[1]] // matr[s, s]
        matr.col_op(pos[1], lambda val, row: val - q * matr[row, s])
        right.col_op(pos[1], lambda val, row: val - q * right[row, s])
        matr.col_swap(s, pos[1])
        right.col_swap(s, pos[1])

        null_edging(matr, left, right, s)


# Iteration of transformation into Smith normal form, modifies edging starting at position [s, s]
def transform_smith(matr: Matrix, left: Matrix, right: Matrix, s: int):
    move_least_to_start(matr, left, right, s)
    # ppr(matr, left, right)

    modify_edging(matr, left, right, s)
    ppr(matr, left, right)

    null_edging(matr, left, right, s)
    ppr(matr, left, right)


# Checks whether south-western block of matrix, starting at pos [s, s], is zero
def next_block_empty_or_null(matr: Matrix, s: int):
    rows, cols = len(matr.col(0)), len(matr.row(0))
    return matr[s + 1: rows, s + 1: cols].is_zero


# Computes Smith's normal form B of matrix A, such that L * A * R = B
# returns:
#  - matrix in Smith normal form (B)
#  - left square matrix (L)
#  - right square matrix (R)
#  - rank of matrix
def smith_form(matr: Matrix):
    matr = matr.copy()
    rows, cols = len(matr.col(0)), len(matr.row(0))
    left, right = Matrix.eye(rows), Matrix.eye(cols)

    if matr.is_zero:
        return matr, left, right, 0

    for s in range(0, min(rows, cols)):
        transform_smith(matr, left, right, s)

        if next_block_empty_or_null(matr, s):
            rank = s + 1
            break

    return matr, left, right, rank


# Solves linear system of equations with use of Smith normal form
def smith_solve(matr: Matrix, bm: list , get_snf=False):
    rows, cols = len(matr.col(0)), len(matr.row(0))
    b = Matrix(bm)

    if rows != len(b):
        raise RuntimeError()

    sf, l, r, rk = smith_form(matr)

    if rk == 0 and not b.is_zero:
        return []
    elif rk == 0 and b.is_zero:
        return Matrix.zeros(cols)
    else:
        #print("line 184")
        #pprint(b)
        #pprint(l)
        c = l * b
        y = Matrix(symbols("y:" + str(cols)))

        if not c[rk: rows] == [0 for i in range(rows - rk)]:
            return []
        else:
            for i in range(0, rk):
                if c[i] % sf[i, i] != 0:
                    return []
                else:
                    y[i] = c[i] / sf[i, i]

            x = r * y
            if get_snf==False :
                return x
            elif get_snf==True :
                return x,sf, l, r, rk


#cols = len(matrix.row(0))
# pprint(smith_form(matrix))
#sol=smith_solve(matrix, b)
#pprint(sol)
#symbol=sol.free_symbols
#pprint(symbol)
#m = matrix, Matrix(b)
#pprint(linsolve(m, symbols("y:" + str(cols))))
""""
Betti_number_SNF=2
d={}
vect=[0]*cols
KerM_SNF=[0]*Betti_number_SNF
list_d=[{}]*Betti_number_SNF
for k in range(Betti_number_SNF):
    counter=0
    for x in symbol:
        print("subs")
        if counter==k :
            d[str(x)]=1
        else:
            d[str(x)]=0
        counter=counter+1
        print(type(x),"=>",x)
    list_d[k]=d.copy()
pprint(list_d)
#sol.subs(d)
i=0
for k in range(Betti_number_SNF):
    vect=[0]*cols
    i=0
    for elem in sol:
        vect[i]=elem.subs(list_d[k])
        print(i,":",elem.subs(list_d[k]))
        i=i+1
    KerM_SNF[k]=Matrix(vect).copy()
pprint(KerM_SNF)
pprint(matrix.nullspace())
"""

#An,L,R,r=smith_form((Matrix(A)))
#print("A")
#pprint(Matrix(A))
#print("SNF")
#print("L.inv()")
#pprint(L.inv())
#print("An")
#pprint(An)
#print("R.inv()")
#pprint(R.inv())
#print("L*An*R")
#print(Matrix(A)==L.inv()*An*R.inv())
#print("Rank",r)

