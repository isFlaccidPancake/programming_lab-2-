'''Write a function that given a matrix of numbers and another number, returns the matrix
obtained by the product of the matrix and the number. E.g.,
Implement two solutions (returning a new matrix and in place modification). '''
def scalar_mult(matrix,n):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=matrix[i][j]*n
    return matrix
def graphical(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print('\n')
matrix=[[10000,12,5], [3,24,2], [5,6,7]]
graphical(scalar_mult(matrix, 5))

    