'''Write a function that returns the transpose of a given matrix. '''
def square_matrix(matrix):
    if len(matrix)==len(matrix[0]):
        return True
    else:
        return False
def graphical(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print('\n')
def transpose(matrix):
    trans=[]
    for i in range(len(matrix[0])):
        new_row=[]
        for j in range(len(matrix)):
                new_row+=[matrix[j][i]]
        trans.append(new_row)
    return trans
matrix=[[10000,12], [3,24], [5,6]]
transposed= transpose(matrix)
graphical(matrix)
print('*'*50)
graphical(transposed)
                  