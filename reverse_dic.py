'''Write a function that inverts a dictionary:
• each distinct value becomes a key;
• for each inverted dictionary key, the value will be a list of the original keys associated with
that value. '''

def transform(d):
    new={}
    for i in d.values():        
        new[i]=[items[0] for items in d.items() if items[1]==i]     
    return new
def compact(d):
    return {i: [items[0] for items in d.items() if items[1]==i] for i in d.values()}
d = {'a':2, 'b':2, 'c':3, 'd':4, 'e':3, 'f':0, 'g':3, 'h':2}       
new=transform(d)
print(new)
print(compact(d))