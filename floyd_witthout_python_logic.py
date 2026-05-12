'''Write a function that prints the Floyd’s Triangle of size n, which is passed as a
parameter. The i-th row of the triangle is a tuple of numbers.
Tip: the first element of each row corresponds to the number of the previous row
(starting to count rows from 1) added to its first element.'''

def floyd(n):
    row=(1,)				#
    print(row)
    new=tuple()
    for i in range(1,n+1):			#every row of the triangle
        for j in range(0,len(row)): #evry element of the previous tuple
            new+= (row[j]+i,)		#generate the new row by following the tip
        row=new + (new[-1]+1,)		#extend to make it a triangle
        new=tuple()					#empty new
        print(row)					#terminal output
n=int(input())
while n<=0:
    n=int(input())
floyd(n)

