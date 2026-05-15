'''Exercise 12.5
• Write a recursive function that given a list L and an element e, returns a new list where
each occurrence of e is removed from L. Do not use for or while'''
def delete(l,e):
    if len(l)==1:
        if l[0]==e:
            return []
        else:
            return [l[0]] #dentro una lista
    return delete(l[:1],e)+delete(l[1:],e)
L=[2,4,5,6,3,5,3,7]
print(delete(L,7))