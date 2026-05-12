'''Write two functions, where given a tuple of integers t and another integer n:
• the first function returns a new tuple in which n is inserted to the head (first
element) of t,
• the second function returns a new tuple in which the head (first element) of t
is replaced by n.
No iteration allowed.'''

def f_1(tuple, n):
    new_tuple= (n,)+tuple
    return new_tuple
def f_2(tuple, n ):
    new_tuple= (n,)+tuple[1:]
    return new_tuple
def function(t1,t2,n):
    if n<0:
        return 'ERROR'
    else:
        new_tuple= t1[:n]+t2+t1[n:]
        return new_tuple
print(function((1, 3, 2),(9, 7),1))