'''
this code will invoke the adjacency matrix based graph
for simplicity , the vertices are numbered through 0-n with n being num of vertices.
edges between vertices are indicated by a 1 in the n*n matrix
'''

from AdjMatrixGraph import AdjMatrix

def doJob():
    nv = int(input('enter the number of vertices for the graph'))
    isDirected = bool(input('enter true if the graph is directed , else enter false'))
    obj = AdjMatrix(nv,isDirected=isDirected)

    # adding edges
    for vertex in range (nv):
        nedge = int(input(f'enter the number of edges for the vertex {vertex}'))
        edge_added = 0
        if nedge == 0:
            continue
        for inner_vtx in range(nv):
            if inner_vtx == vertex:
                continue
            val = int(input(f' is edge needed from {vertex} to {inner_vtx} ?. enter 1 if needed else 0'))
            if val == 1 and edge_added<nedge:
                obj.addEdge(vertex,inner_vtx)
                edge_added+=1
            else:
                if val !=0:
                  print(f' max edges exceeded')
                else:
                    pass
    # get indegree
    for vertex in range(nv):
        obj.getInDegree(vertex)

    # get adjacent vertices
    for vertex in range(nv):
        obj.getAdjacentVertices(vertex)

    # check adjacency
    vtx = int(input(f' enter the source vertex'))
    dvtx = int(input(f' enter the destn vertex'))
    obj.isVertexAdjacent(vtx,dvtx)

    # remove edges
    for vertex in range (nv):
        nedge = int(input(f'enter the number of edges to remove for the vertex {vertex}'))
        if nedge == 0:
            continue
        edge_removed = 0
        for inner_vtx in range(nv):
            if inner_vtx == vertex:
                continue
            val = int(input(f' is edge to be removed from {vertex} to {inner_vtx} ?. enter 1 if needed else 0'))
            if val == 1 and edge_removed<nedge:
                obj.removeEdge(vertex,inner_vtx)
                edge_removed+=1
            else:
                if val !=0:
                  print(f' max edges exceeded')
                else:
                    pass

    obj.showGraph()

if __name__ == '__main__':
    doJob()



