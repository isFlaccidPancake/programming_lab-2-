def vector_scalar(vec1,vec2):		#maybe i insert trasnpose here
    if len(vec1)==len(vec2):
        scalar=0
        for i in range(len(vec1)):
            scalar+= vec1[i]*vec2[i]
        return scalar
    else:
        print('NOT COMPATIBLE DIMENSIONS FOR THIS OPERATION')
def transpose(matrix):#instead of multiplying the row for the column which would be tedious
    trans=[]			#we make a row of every column, to easily access them as vectors
    for i in range(len(matrix[0])):
        new_row=[]
        for j in range(len(matrix)):
                new_row+=[matrix[j][i]]
        trans.append(new_row)
    return trans
def matrix_mult(matrix1,matrix2):
    if len(matrix1[0])==len(matrix2):#check conditions of matrix multiplications
        transposed= transpose(matrix2)#transpose of the right matrix 
        result=[]
        for i in range(len(matrix1)):#every row in the first matrix one at a time
            new_row=[]
            for j in range(len(matrix2[0])):#multiplied by every column of the second matrix
                new_row+=[vector_scalar(matrix1[i],transposed[j])]#making as many scalars as the number of columns in matrix2
            result.append(new_row)				#add the new row with the scalars in the matrix
        return result
    else:
        print('NOT COMPATIBLE DIMENSIONS FOR THIS OPERATION\nOR NOT RIGHT MATRIX ORDER')
def graphical(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print('\n')
matrix1=[[10000,12], [3,24], [5,6],[3,1]]
matrix2=[[23,45,7],[5,8,2]]
graphical(matrix_mult(matrix1,matrix2))#worked first try the new function matrix_mult
