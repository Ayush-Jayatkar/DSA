sparse_matrix = {
    (0,3):5, (2,1):3
}

def get_value(matrix, row, coln):
    return matrix.get((row, coln), 0)

def setvalue(matrix, row, coln,value):
    if value != 0:
        matrix[(row, coln)] = value
    elif (row, coln) in matrix:
        del matrix[(row, coln)]

def sparse_matrix(matrix, row, colm):
    for row in range(row):
        for coln in range(coln):
            print(get_value(matrix, row, coln,), end=' ')
            print()
    
row, coln = 4, 4 

print("Sparse Matix=")
sparse_matrix(sparse_matrix, row, coln)