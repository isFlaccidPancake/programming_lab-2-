'''Exercise (H3.6)
Write a function that given a nested tuple (which may contain tuples containing tuples
etc), prints the elements of the tuple.  You need to first flatten the tuple. 
E.g., given the tuple (1, 2, (3.1, 3.2), 4, 5, (6.1, (6.2,1, 6.2,2), 6.3), 7), the function prints
1 2 3.1 3.2 4 5 6.1 6.2.1 6.2.2 6.3 7 '''


def read(t):
    for e in t:
        if type(e)!=tuple:
            print(e, end=' ')
        else:
            read(e)
n=eval(input())
read(n)