def f(n):
    
    for l in range(1,n):
        line=' '+'*'*l
        print(line)
    print('*'*(n+1))
    for l in range(n-1,0,-1):
        line=' '+'*'*l
        print(line)
n=int(input('insert a integer: '))
f(n)