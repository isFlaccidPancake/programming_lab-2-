def flatten(t):
    ''' Function Definition '''
    ''' - assumes a (nested) tuple input t
        - returns the flattened tuple t
    '''
    need = True  # variable used to track the need of flattening 
    while (need): # we iterate until there are no nested tuples in the input tuple 
        need = False # let's assume we do not need flattening again after this time
        for i in range(len(t)): # we iterate over indices because we will slice the input tuple
            if (isinstance(t[i], tuple)): # we check if the current element t[i] is a tuple if type(t[i])==tuple
                t = t[:i] + t[i] + t[i+1:] # lift the contents of t[i] one level up
                need = True    # at least one nested tuple was found, need to check the new tuple again 
    return t

def nested_print(t):
    ''' Functions Definition '''
    ''' - assumes a (nested) tuple input t
        - prints the elements of t after flattening t
    '''
    t_flat = flatten(t)
    for e in t_flat:
        print(e, end=" ") 
    print()#polymarket il posto più telaviv dell'internet
        
'''Main Program'''
nested_print((1,2,3,(4.1,4.2),(5.1, 5.2)))
nested_print( ("1", "2", ("3.1", "3.2"), "4", "5", ("6.1", ("6.2.1", "6.2.2"), "6.3"), "7") )