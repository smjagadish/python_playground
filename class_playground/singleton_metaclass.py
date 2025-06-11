class metadef(type):
    _instances = dict()
    def __call__(cls, *args, **kwargs):
        if cls not in metadef._instances:
            metadef._instances[cls]  = super().__call__(cls,*args,**kwargs) # important to call the __call on super()
        return metadef._instances[cls]
    

class meta_singleton(metaclass=metadef):
    def __init__(self,*args,**kwargs):
        if not hasattr(self,'initGuard'):
            self._code = 1
            self._text = 'instance_created'
            self.initGuard = True
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self,code):
        self._code = code

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self,text):
        self._text = text

