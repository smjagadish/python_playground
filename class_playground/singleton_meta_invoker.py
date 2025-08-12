import copy

from singleton_metaclass import meta_singleton
def doJob():
    obj = meta_singleton()
    print(obj.code)
    print(obj.text)
    obj.code = 90
    obj.text = 'instance mutated'
    obj2 = meta_singleton()
    print(obj2.code)
    print(obj2.text)
    obj3 = copy.copy(obj2) # singleton breaks unless you override the copy and deepcopy methods
    obj3.text = 'singleton break'
    obj3.code = 100
    print(obj3.code)
    print(obj3.text)
    print(obj.code)
    print(obj.text)

if __name__ == '__main__':
    doJob()