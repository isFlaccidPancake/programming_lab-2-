'''Write a function that prints the contents of a given matrix with proper spacing.
 E.g., given [[10000,12], [3,2], [5,6]] the function prints:
 
1000	12
3		2
5		6
• Tip: use print(e, end=‘\t’)'''

def graphical(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print('\n')
graphical([[10000,12], [3,2], [5,6]])
    