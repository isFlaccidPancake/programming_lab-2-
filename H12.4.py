'''Write a recursive function that given a tuple t of numbers and another number n, returns
a new tuple where each element of t has been multiplied by n. Do not use for or while.
 E.g., given t = (4, 2, 5, 3) and n = 2, the function returns (8, 4, 10, 6).  '''
def multiply_t(t,n):
    if len(t)==1:
        return (t[0]*n,)
    return (t[0]*n,)+multiply_t(t[1:],n)
print(multiply_t((4, 2, 5, 3) ,2))