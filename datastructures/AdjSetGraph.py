'''
this code is a concrete implementation for the graph abstract base class
'''
from queue import Queue

from Graph import Graph
from GraphVertex import vertex
class AdjSet(Graph):

    def __init__(self, nvertices,isDirected):
        super().__init__(nvertices,isDirected)
        self.vertices = list()

    def createVertex(self,data):
        if len(self.vertices) <= self.nvertices:
            self.vertices.append(
            vertex(data=data)
        )

    def addEdge(self,elem,elem_dest):
        if elem == elem_dest:
            print('cannot add edge to self')
            return
        for idx in self.vertices:
            if idx.data == elem:
                src_index = self.getSrcidx(elem)
                dest_idx = self.getidx(elem_dest)
                if dest_idx != -1:
                  self.vertices[src_index].addEdge(elem_dest)
                  return
                else:
                  print(f' condition not satisfied to add edges. try again after adding the vertices')

    def getidx(self, elem_dest):
        for idx in range(len(self.vertices)):
            if elem_dest == self.vertices[idx].data:
                return idx
        return -1

    def getSrcidx(self,elem):
        for idx in range(len(self.vertices)):
            if elem == self.vertices[idx].data:
                return idx
        return -1

    def getSrcObj(self,elem):
        for idx in self.vertices:
            if elem == idx.data:
                return idx
        return -1

    def removeEdge(self,elem,elem_dest):
        if elem == elem_dest:
            print('cannot remove an edge to self')
            return
        for idx in self.vertices:
            if idx.data == elem:
                src_index = self.getSrcidx(elem)
                dest_idx = self.getidx(elem_dest)
                if dest_idx != -1:
                  self.vertices[src_index].removeEdge(elem_dest)
                  return
                else:
                  print(f' condition not satisfied to remove edges. try again after adding the vertices')


    def getAdjacentnodes(self,elem):
        if self.getidx(elem) == -1:
            print('vertex not found. add and then search for adjacent nodes')
            return
        else:

            for i in range(len(self.vertices)):
                if self.vertices[i].data == elem:
                    vals = self.vertices[i].edges
                    print(f'the list of adjacent nodes is:{vals}')
                    break

    def isAdjacent(self,elem,elem_dest):
        if self.getidx(elem) == -1:
            print(f' vertex not found to check adjacency check.add vertex and then do check')
            return
        else:

            for i in range(len(self.vertices)):
                if self.vertices[i].data == elem:
                  if elem_dest in self.vertices[i].edges:
                    print(f' the node {elem_dest} is adjacent to {elem}')
                  else:
                    print(f' the node {elem_dest} is not adjacent to {elem}')
                break

    def getIndegree(self,elem):
        if self.getidx(elem) == -1:
            print(f' the vertex is not found to do indegree ops')
            return
        else:
            idx = 0
            for node in self.vertices:
                if elem in node.edges:
                    idx+=1
            print(f' the indegree for {elem} is {idx}')
            return idx

    def getVertices(self):
        return self.vertices

    def printGraph(self):
        print(f' printing the graph and its vertices')
        for idx in self.vertices:
            print(f'node :{idx.data}',end=' ')
            if len(idx.edges)!=0:
                print(f'edges: {idx.edges}')
            else:
                print(f'no edges')

    def bfs(self):
        if self.vertices is not None:
            root_idx = self.vertices[0]
            vertex_queue = Queue()
            visited_vertex = set()
            vertex_queue.put(root_idx)
            while not vertex_queue.empty():
                elem = vertex_queue.get()
                print(f'{elem.data}->',end='')
                for edge in elem.edges:
                    if edge not in visited_vertex:
                      vertex_queue.put(self.getSrcObj(edge))
                      visited_vertex.add(edge)

    def dfs(self):
        if self.vertices is not None:
            root_idx = self.vertices[0]
            self.doDfs(root_idx)

    def doDfs(self,idx,visited_nodes=set()):
        if idx is not None:
            print(f'{idx.data}->',end='')
            visited_nodes.add(idx.data)
            for edge in idx.edges:
                if edge not in visited_nodes:
                  edge_obj = self.getSrcObj(edge)
                  self.doDfs(edge_obj,visited_nodes)

    def func(self,val1,val2):
        if val1 < val2:
            return val2

    def doTopologicalSort(self):
        indeg_dicts = dict()
        '''for vx in self.vertices:
            indegree = self.getIndegree(vx.data)
            if indegree == 0:
                print(f'{vx.data}->',end='')
                vx.edges.clear()
                '''
        #sorted_dicts = dict(sorted(indeg_dicts.items(),key= lambda x:x[1]))
        self.performSort(self.vertices[0])

    def performSort(self,vx):
        if self.getIndegree(vx.data) == 0:
            print(f'{vx.data}->',end='')
            for edge in list(vx.edges):
                vx.edges.remove(edge)
                self.performSort(self.getSrcObj(edge))


















