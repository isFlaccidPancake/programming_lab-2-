'''Write a function that given a tuple t behaves as follows:
• returns None if t is not a tuple, DO NOT DO IT
• verifies that t contains only integers (using a while loop), otherwise returns
False,
• returns True if in t each element (except the first) is greater than the sum of
the previous elements (using a while loop), otherwise returns False.'''
def fun(t):
    a=integers(t)
    b=greater(t)
    return a and b
    
def integers(t):
    condition= True
    count=0
    while condition and count<len(t):
        if t[count]!=int:
            condition=False
        else:
            count+=1
    return condition
def greater(t):
    condition= True
    count=1
    total=0
    while condition  and count<len(t):
        total+= t[count-1]
        if t[count]<=total:
            condition=False
        else:
            count+=1
    return condition

tuplee= eval(input())
print(fun(tuplee))
        
        
        
        
    
        