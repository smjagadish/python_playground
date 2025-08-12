import copy
from singleton_class_with_new import singleton_new
def doJob():
    obj = singleton_new()
    print(f' contents after construction')
    obj.__repr__()
    print(f' manipulating with existing object')
    obj.code = 100
    obj.text = 'new world'
    print(f' contents after manipulation')
    obj.__repr__()
    obj2 = singleton_new()
    print(f' second instance constructed, but it really is a singleton')
    obj2.__repr__()
    '''
    this code is singleton protected shallow or deep copy doesn't matter
    there is no escape route in other words 
    obj3 = copy.deepcopy(obj2)
    obj3.code = 200
    obj3.text = 'bad world'
    obj3.__repr__()
    obj2.__repr__()
    obj.__repr__()
    '''

if __name__ == '__main__':
    doJob()

