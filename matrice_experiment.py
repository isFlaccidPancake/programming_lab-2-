def row_swapping(matrix,row1,row2):
    matrix[row1],matrix[row2]=matrix[row2],matrix[row1]
    return matrix
    
def scalar_multiplication(matrix,row1,scalar):
    for i in range(len(matrix[row1])):
        matrix[row1][i]=matrix[row1][i]*scalar
    return matrix
def row_addition(matrix, row1,row2,scalar):
    for i in range(len(matrix[row1])):
        matrix[row1][i]=matrix[row1][i]+(scalar*matrix[row2][i])
    return matrix
def REF(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,i):
            if matrix[i][j]!=0:
                return False 
    else:
        return True
def upper_triangular(matrix):
    if len(matrix)==len(matrix[0]):
        return REF(matrix)
    else:
        return False
def gaussian_algorithm_toREF_uptr(matrix):
    while not upper_triangular(matrix) or not REF(matrix):
        
    return new_matrix, tracking_coefficent


def RREF(matrix):
    matrix=gaussian_algorithm_toREF_uptr(matrix)
    return matrix



def determinant(matrix):
    REF,tracking_coefficent=gaussian_algorithm_toREF_uptr((matrix))
    determinant=1
    for i in range(matrix):
        determinant*=REF[i][i]
    determinant*=tracking_coefficent
    return determinant
        
        

matrice=[[3,2,3,1],[0,4,5,3],[0,0,3,6],[0,0,0,3]]
print(upper_triangular((matrice)))
