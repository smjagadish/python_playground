import copy

from singleton_class_with_decorator import singleton_with_dec
def doJob(ncode,ntext):
    obj = singleton_with_dec(ncode=ncode,ntext=ntext)
    obj.__repr__()
    obj.setncode(23)
    obj.setntext('testing')
    obj1 = singleton_with_dec(ncode=ncode,ntext=ntext)
    obj1.__repr__()
    '''
    the code snippets below show the dangers of singleton pattern with decorators without proper control
    '''
    #obj2 = singleton_with_dec.__new__(singleton_with_dec) # won't work as the decorator returns a fn object and not class
    obj2 = copy.copy(obj) # to avoid break of singleton pattern due to this step , you can override __copy and __deepcopy to return self
    obj2.__init__(ncode=45,ntext='evil')
    obj2.__repr__() # singleton broken . obj2 is a diff instance
    obj.__repr__() # not impacted . singleton
    obj1.__repr__() # not impacted . singleton

if __name__ == '__main__':
    doJob(1,'hello')