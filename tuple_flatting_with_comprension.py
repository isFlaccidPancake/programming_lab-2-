'''Write a function that given a tuple of ranges, returns a tuple which contains all the values
included in the given ranges.
E.g., given (range(1,5), range(10,12), range(20,31)), the function returns the
tuple (1,2,3,4,10,11,20,21,22,23,24,25,26,27,28,29,30)'''
def f(sequence):
    return tuple(e for rangee in sequence for e in rangee)

def ff(sequence):
    t=()
    for rangee in sequence:
        for e in rangee:
            t+= (e,)
    return t
print(f((range(1,5), range(10,12), range(20,31))))
print(ff((range(1,5), range(10,12), range(20,31))))
