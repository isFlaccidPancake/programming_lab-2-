'''Write a function that given a tuple of tuples formed by a string and a number, e.g.,
((“a”, 13),(“b”, 22),(“c”, 30)), returns a tuple containing the average and the maximum
of the numbers in the tuples, as well as the string belonging to the tuple with the
maximum number.
E.g., given the tuple above, the function returns the tuple (21.666, 30, “c”).'''

def maxi(t):
    associato=''
    massimo=0
    for e in t:
        if e[1]>massimo:
            massimo=e[1]
            associato= e[0]
    return (massimo, associato)
def av(t):
    av=0
    for e in t:
        av+= e[1]
    av= av/len(t)
    return (av,)
def tot(t):
    return av(t)+ maxi(t)

t= (('a', 13),('b', 22),('c', 30))

print(tot(t))