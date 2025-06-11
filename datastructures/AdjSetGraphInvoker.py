'''
invoking class for instantiating a graph backed by adjacency set
'''
from AdjSetGraph import AdjSet
def doJob():
    num_vertex = int(input('enter the number of vertices the graph will have'))
    type = bool(input('enter true if the graph is directed or false if it is not'))
    obj = AdjSet(num_vertex,type)

    # adding vertices
    print(f' adding vertices to graph')
    for i in range(num_vertex):
        val = str(input('enter the vertex qualifier'))
        obj.createVertex(val)

    # adding edges
    print(f' adding edges for each vertex added')
    for i in range(num_vertex):
      print(obj.getVertices()[i].data)
    for i in range(num_vertex):
        nv = int(input(f'enter the number of edges for vertex {obj.getVertices()[i].data}'))
        for j in range(nv):
            ed = str(input(f'enter the edge node'))
            obj.addEdge(obj.getVertices()[i].data,ed)

    # print adjacent nodes
    print(f' printing adjacent nodes for each vertex added')
    for i in range(num_vertex):
        elem = obj.getVertices()[i].data
        obj.getAdjacentnodes(elem)


    # check adjacency
    elem = str(input('enter the vertex to find adjacency for'))
    elem_dest = str(input('enter the vertex to check adjacency'))
    obj.isAdjacent(elem,elem_dest)

    # get indegree
    print(f' printing indegree for each vertex added')
    for i in range(num_vertex):
        elem = obj.getVertices()[i].data
        obj.getIndegree(elem)


    # removing edges
    print(f' removing edges for each vertex added')
    for i in range(num_vertex):
        nv = int(input(f'enter the number of edges to remove for vertex {obj.getVertices()[i].data}'))
        for j in range(nv):
            ed = str(input(f'enter the edge node'))
            obj.removeEdge(obj.getVertices()[i].data, ed)

    # print graph
    obj.printGraph()

    #breadth first search
    print(f'doing breadth first search')
    obj.bfs()
    print()

    # depth first search
    print(f' doing depth first search')
    obj.dfs()
    print()

    #topological sort
    print(f' doing a topological sort')
    obj.doTopologicalSort()
    print()


if __name__ == '__main__':
    doJob()