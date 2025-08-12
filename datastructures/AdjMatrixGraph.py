'''
implementation of graph using adjacency matrix
'''
import numpy as np

from Graph import Graph
from datastructures.GraphVertex import vertex


class AdjMatrix():

    def __init__(self, nvertices, isDirected=False):

        self.nvertices = nvertices
        self.isDirected = isDirected
        self.vertices = np.zeros((nvertices,nvertices),dtype=np.int64)

    def addEdge(self,v1,v2):
        if v1 > self.nvertices or v2 >self.nvertices or v1 <0 or v2 <0:
            print(f'invalid edge addition, try later')
            return
        else:
            self.vertices[v1,v2] = 1

    def removeEdge(self,v1,v2):
        if v1 >self.nvertices or v2> self.nvertices or v1 < 0 or v2 < 0:
            print(f' invalid edge removal , try later')
            return
        else:
            if self.vertices[v1,v2] !=1 :
                print(f' non-existent edge, nothing to remove')
                return
            else:
              self.vertices[v1,v2] = 0

    def getInDegree(self,idx):
        if idx >self.nvertices or idx<0 :
            print(f' invalid vertex for indegree calc, try later')
            return
        else:
            ret_val = self.vertices[idx,:]
            rv = [ val for val in ret_val if val !=0]
            print(f' the indegree info for {idx} is {len(rv)}')

    def getAdjacentVertices(self,idx):
        if idx > self.nvertices or idx <0 :
            print(f' invalid vertex to find adjacent nodes, try later')
            return
        else:
            adj_v = self.vertices[idx,:]
            print(f' the list of adjacent vertices for {idx} is {adj_v}')

    def isVertexAdjacent(self,idx1,idx2):
        if idx1 >self.nvertices or idx2 >self.nvertices or idx1<0 or idx2<0:
            print(f' invalid vertex info to calcualte adjacency')
            return
        else:
            if self.vertices[idx1,idx2] == 1:
                print(f' the vertex {idx2} is adjacent to {idx1}')
            else:
                print(f' the vertex {idx2} is not adjacent to {idx1}')

    def showGraph(self):
        print(f' the graph with edges and vertices is: {self.vertices}')





