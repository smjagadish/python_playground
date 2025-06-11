'''
 this code snippet is demonstrating use of class variables , instance variables
 it also shows python's quirks of promoting class variables to instance variables under certain circumstances
'''
class basic:
    basic_var = 45
    def __init__(self):
        self.var1 = 0
        self.var2 = 'text'
        self.var3 = 3.4
    def getData(self):
        print(f'the values are{self.__dict__}')
        print(f'the class var value is {self.basic_var}')

    def changeClassvar(self,val):
        basic.basic_var = val


    def changeClassvarWithself(self,val):
        basic.basic_var = val
        self.basic_var = val #  i use self.basic_var then there will be promotion

if __name__ == '__main__':
    obj1 = basic()
    obj2 = basic()
    obj1.getData()
    obj2.getData()
    obj2.changeClassvar(24) # affects both obj
    obj1.getData()
    obj2.getData()
    obj1.changeClassvarWithself(33) # affects obj1 as i use self in method . will also change obj2 content to 33
    obj1.getData()
    obj2.getData()
    obj2.basic_var = 67 # this is where the class var gets promoted as instance var. affects only obj2
    obj1.getData()
    obj2.getData()

