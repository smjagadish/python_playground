"""
super-simple structure of a binary tree node
"""
class binaryTree:
    def __init__(self):
        self.__data = None
        self.__right = None
        self.__left = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self,value):
        self.__right = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self,value):
        self.__left = value
