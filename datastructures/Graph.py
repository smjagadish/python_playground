'''
abstract base class for the graph.
concrete impl will be based on this.
capabilities provided include adding edge , removing edge , getting adjacent edges, cehcking if an edge is adjacent
the graph can be directed or non-directed. choice is made during graph creation
'''

from abc import abstractmethod , ABC
import numpy as np
class Graph(ABC):
    def __init__(self,nvertices,isDirected=False):
        self.nvertices = nvertices
        self.isDirected = isDirected

    @abstractmethod
    def addEdge(self,elem,elem_dest):
        pass

    @abstractmethod
    def removeEdge(self,elem,elem_dest):
        pass

    @abstractmethod
    def isAdjacent(self,elem,elem_dest):
        pass

    @abstractmethod
    def getAdjacentnodes(self,elem):
        pass

    @abstractmethod
    def getIndegree(self,elem):
        pass

    @abstractmethod
    def createVertex(self,data):
        pass

    @abstractmethod
    def printGraph(self):
        pass

    @abstractmethod
    def bfs(self):
        pass