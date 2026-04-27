'''Exercise (H3.6)
Write a function that given a nested tuple (which may contain tuples containing tuples
etc), prints the elements of the tuple.  You need to first flatten the tuple. 
E.g., given the tuple (1, 2, (3.1, 3.2), 4, 5, (6.1, (6.2,1, 6.2,2), 6.3), 7), the function prints
1 2 3.1 3.2 4 5 6.1 6.2.1 6.2.2 6.3 7 '''

lista=[]
def flat(t):
    for i in range(len(t)):
        if type(t[i])== tuple:
           flat(t[i])			#until i dont find a !=tuple I go deeper
        else:
            lista.append(t[i])		#any return would break the original for-cycle at the first recursion
t=eval(input('insert tuple: '))
flat(t)
for i in lista:
    print(i, end='--')

