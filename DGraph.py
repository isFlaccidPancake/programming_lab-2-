'''
 The internal graph structure should be private to the class and can be represented using
any data structure of your choice. Try and choose the one that suits the best. The class should
contain a constructor of an empty directed graph and the following methods:
newNode(n) # creates a node with label 'n' in the graph
newEdge(s,d) # creates a directed edge from node 's' to node 'd'
 # in the graph
getNodes() # returns the list of all the nodes of the graph
getOut(n) # returns the list of the nodes having an edge from
 # the node 'n' in the graph
 '''
class DGraph:
    def __init__(self):
        '''just an empty directed graph'''
        self.__nodes={}
    #implemented the graph as an empty dictionary, each key is a node, the value will be a list with the other nodes the edges go towards
    def getNodes(self):
        '''returns the list of all the nodes of the graph'''
        return list(self.__nodes.keys())
    def getOut(self,n):
        '''returns the list of the nodes having an edge from the node 'n' in the graph'''
        return self.__nodes[n]
    def newNode(self,n):
        '''creates a node with label 'n' in the graph'''
        if n not in self.getNodes():
            self.__nodes[n]=[]
    def newEdge(self,s,d):
        '''creates a directed edge from node 's' to node 'd' in the graph'''
        self.newNode(s)# if source and destination dont exist newEdge adds them on its own
        self.newNode(d)
        if d not in self.getOut(s):#avoid redunadant edges when two nodes are already linked
            self.getOut(s).append(d)