'''Exercise 12.6
• Write a recursive function Fibonacci(n) that given a non-negative integer n, returns a
list containing the sequence of values from Fibonacci(0) to Fibonacci(n) where: 
'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
def fib_list(n):
    lista=[]
    for i in range(0,n+1):
        lista.append(fib(i))
    return lista
print(fib_list(13
               ))
