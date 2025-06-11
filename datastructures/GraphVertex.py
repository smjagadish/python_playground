'''
this class models the vertices of a graph using adjacency set.
it can be easily repurposed to an adjacency list by storing the edges in a list instead of a set.
the attributes are the data a vertex holds and the list of edges it has.
the edges coukd be weighted , which comes into play for shortest path algorithms etc.
'''

class vertex:
    def __init__(self,*args,**kwargs):
        self._data = kwargs['data']
        self._edges = set()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,val):
        self._data = val

    def addEdge(self,elem):
        self.edges.add(elem)

    def removeEdge(self,elem):
        self.edges.remove(elem)

    def isEdgePresent(self,elem):
        return True if elem in self.edges else False

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self,val):
        self._edges = val

