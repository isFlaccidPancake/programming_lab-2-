n= int(input())
villages=[]
for i in range(n):
    villages.append(int(input()))
villages.sort()
left = (villages[1]-villages[0])/2
right= (villages[2]-villages[1])/2
min_= left+right
for i in range(2, n-1):
    left= (villages[i]-villages[i-1])/2
    right= (villages[i+1]-villages[i])/2
    size= left+right
    if size< min_:
        min_=size
print(min_)