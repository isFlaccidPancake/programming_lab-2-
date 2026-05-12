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
print(f_1((0,1,2),3))
print(f_2((0,1,2),3))