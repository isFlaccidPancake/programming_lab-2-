'''Write a recursive function that returns the minimum element of a given sequence (tuple,
list, string, ...). Do not use for, while, min, max. '''
def minimum(seq):
    if len(seq)==1:
        return seq
    if int(seq[0])<int(minimum(seq[1:])):
        return seq[0]
    else:
        return minimum(seq[1:])
print(minimum('67892'))
        