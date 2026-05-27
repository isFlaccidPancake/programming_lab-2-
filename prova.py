from DGraph import *
def allIn(n,g):
    origins=[]
    for i in g.getNodes():
        if n in g.getOut(i):
            origins.append(i)
    return origins
def enormous(g,n):
    for i in range(1,10000):
       g.newEdge(n,i) 
example= DGraph()
example.newEdge('a','b')
example.newEdge('a','c')
example.newEdge('a','d')
example.newEdge('a','c')
enormous(example,'a')

example.newEdge('c','d')
example.newEdge('c','d')
example.newEdge('b','d')
#3 I use another method from the class
print(example.getOut('a'))
#4 I use another method from the class
print(example.getNodes())
#5 I use the function defined in the programm
print(allIn('d',example))