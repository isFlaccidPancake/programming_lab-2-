'''Ex 10.11 Write a function that verifies that the sum of the numbers from 1 to a given non-negative
number n is equal to n(n+1)/2'''

def f(n):
    a=sum(i for i in range(0,n+1))
    b=(n*(n+1))/2
    return a==b
print(f(7))