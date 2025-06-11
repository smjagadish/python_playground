"""
this code invokes the binary tree operations
"""
from binarytreehelper import binarytreeHelper
def addNode(parent):
    print(f' adding node to binary tree')
    val = int(input('enter data of the node to add'))
    parent.addNode(parent.getRoot(),val)

def printNode(parent):
    print(f' printing the binary tree from left to right')
    parent.printNodes(parent.getRoot())

def searchNode(parent):
    data = int(input('enter the value of the node to search'))
    vals= parent.searchNode(parent.getRoot(),data)
    if vals !=1:
        print(f' node is not present , search failed')


def minNode(parent):
    print(f' will check the min value in the node')
    parent.minNode(parent.getRoot())

def maxNode(parent):
    print(f' will check the max value in the node')
    parent.maxNode(parent.getRoot())

def maxDepth(parent):
    print(f' the max depth of the bst is {parent.maxDepth(parent.getRoot())}')

def sumPaths(parent):
    print(f' printing sum of paths')
    parent.sumPaths(parent.getRoot())

def bfs(parent):
    print(f' breadth first traversal')
    parent.bfs(parent.getRoot())
    print()

def inorder(parent):
    print(f' in order traversal')
    parent.print_in_order(parent.getRoot())

def postorder(parent):
    print(f' post order traversal')
    parent.print_post_order(parent.getRoot())

if __name__ == '__main__':
    parent = binarytreeHelper()
    num_nodes = int(input('enter number of nodes to insert'))
    for node in range(num_nodes):
        addNode(parent)
    printNode(parent)
    searchNode(parent)
    minNode(parent)
    maxNode(parent)
    maxDepth(parent)
    sumPaths(parent)
    bfs(parent)
    inorder(parent)
    postorder(parent)
