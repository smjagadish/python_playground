"""
binary search tree implementation
this uses the binary tree node as defined in the binarytree class
"""
import queue
from array import array

from binarytree import binaryTree
class binarytreeHelper:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def addNode(self,node,data):
        if self.getRoot() is None:
            obj = binaryTree()
            obj.data = data
            obj.right = None
            obj.left = None
            self.__root = obj
            return
        if data <= node.data:
            if node.left is None:
                obj = binaryTree()
                obj.data = data
                obj.left = None
                obj.right = None
                node.left = obj
                return
            self.addNode(node.left,data)
        else:
            if node.right is None:
                obj = binaryTree()
                obj.data = data
                obj.left = None
                obj.right = None
                node.right = obj
                return
            self.addNode(node.right,data)

    def printNodes(self,node):
        if node is not None:
            print(f'{node.data}->',end='')
            self.printNodes(node.left)
            self.printNodes(node.right)

    def searchNode(self,node,data):
        match = 0
        if node is  None:
            return 0
        if node.data == data:
            print(f' the node with data {data} is present in the tree . will quit search now')
            return 1
        elif node.data >= data:
            return self.searchNode(node.left,data)
        else:
           return self.searchNode(node.right,data)


    def minNode(self,node):
        if self.getRoot() is None:
            print(' no nodes to do min search')
            return
        if node.left is None:
            print(f' the node with min value is {node.data}')
        else:
            self.minNode(node.left)

    def maxNode(self,node):
        if self.getRoot() is None:
            print(' no nodes to do max search')
            return
        if node.right is None:
            print(f' the node with max value is {node.data}')
        else:
            self.maxNode(node.right)

    def maxDepth(self,node,depth=0):
        ldepth=rdepth=0
        if self.getRoot() is None:
            print(f' the max depth is 0. add nodes to compute max depth')

        if node is not None:
            if node.right is None and node.left is None:
                return depth
            depth+=1
            ldepth += self.maxDepth(node.left,depth)
            rdepth += self.maxDepth(node.right,depth)
        return ldepth if ldepth>rdepth else rdepth

    def sumPaths(self,node,sum=0):
        if self.getRoot() is None:
            print(f' there are no nodes added to tree. add node to compute sum')
        if node is not None:
            sum+= node.data
            if node.left is None and node.right is None:
                print(f'sum of paths from root to {node.data} is : {sum}')
            self.sumPaths(node.left,sum)
            self.sumPaths(node.right,sum)

    def bfs(self,node,queue_node=queue.Queue()):
        if self.getRoot() is None:
            print(f'the bst is empty, no bfs possible. add nodes and then try')
        queue_node.put(node)
        while queue_node.qsize() !=0:
            elem = queue_node.get()
            print(f'{elem.data}->',end='')
            if elem.left is not None:
              queue_node.put(elem.left)
            if elem.right is not None:
                queue_node.put(elem.right)

    def print_in_order(self,node):
        if self.getRoot() is None:
            print(f' the tree is empty. add nodes to do in order traversal')
            return
        if node is not None:
            self.print_in_order(node.left)
            print(f'{node.data}->',end='')
            self.print_in_order(node.right)

    def print_post_order(self,node):
        if self.getRoot() is None:
            print(f' the tree is empty. add nodes to do post order traversal')
            return
        if node is not None:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(f'{node.data}->', end='')











