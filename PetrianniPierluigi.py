'''
 Define a function named allIn(n,g) that, given a node n and a directed graph g, returns
a list of the nodes that are the source of the edges directed to the given node in the graph.
For instance, given the node 'd' and the graph shown in the example, the function would
return the list ['a','b','c'].
2. Create a directed graph as shown in the example.
3. Print the list of the nodes directing from the node 'a' in the graph. Following the example,
it is ['b','c','d'].
4. Print all the nodes of the graph. In the example, it is ['a','b','c','d'].
5. Print all the nodes directing to the node 'd' in the graph. In the example, it is
['a','b','c'].
Note that, since those lists represent set, the order of the nodes is irrelevant.

'''
from DGraph import *
#1 I define such function; by iterating trought all the nodes of the graph I check if any of them as an edge toawards n inside the graph g
#this function is higly unefficent for a graph, but as our example is very small (4 edges) so I dont care
def allIn(n,g):
    origins=[]
    for i in g.getNodes():
        if n in g.getOut(i):
            origins.append(i)
    return origins
#2 I build the example graph using the methods of the DGraph class
example= DGraph()
example.newEdge('a','b')
example.newEdge('a','c')
example.newEdge('a','d')
example.newEdge('c','d')
example.newEdge('b','d')
#3 I use another method from the class
print('Nodes directing from node a:', example.getOut('a'))
#4 I use another method from the class
print('Nodes of the graph:',example.getNodes())
#5 I use the function defined in the programm in point 1
print('Nodes arriving to node d:', allIn('d',example))
#done
