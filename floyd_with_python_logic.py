def floyd(n):
    j=1
    for i in range(1,n+1):
        print(i , tuple(range(j,j+i)))
        j=j+i
        
        
n=int(input())       
floyd(n)
