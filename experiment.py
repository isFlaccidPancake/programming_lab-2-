'''Write a function that given a tuple of numbers, which represents grades, returns
the average grade. Ask the user to insert the grades as a tuple and parse the
input with eval( ).'''
def average(tuple):
    tot=0
    for i in tuple:
        tot+=int(i)
        result=tot/len(tuple)
    return result
grades_vec= eval(input('insert the grades as a tuple'))
print(average(grades_vec))


