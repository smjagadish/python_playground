def decorator_singleton(cls):
    _instances = dict()
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args,**kwargs)
        return _instances[cls]
    return wrapper

@decorator_singleton
class singleton_with_dec:
    def __init__(self,*args,**kwargs):
        self._ncode = kwargs['ncode']
        self._ntext = kwargs['ntext']


    def getncode(self):
        return self._ncode

    def setncode(self,code):
        self._ncode = code

    def getntext(self):
        return self._ntext

    def setntext(self,text):
        self._ntext = text

    def __repr__(self):
        print(f'dumping the object content')
        print(f'ncode is : {self._ncode} and ntext is: {self._ntext}')

    '''
    consider overriding copy and deepcopy to avoid the singleton pattern to break
    '''




