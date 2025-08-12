class singleton_new:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls,*args,**kwargs)
        else:
            pass
        return cls._instance

    def __init__(self,*args,**kwargs):
        if not hasattr(self, '_initialized'):  # this is key - if i dont have a logic of this sort, there is risk of init to be called again even if the same object instance is being retrieved
          self.__code = 1
          self.__text = 'hello world'
          self._initialized = True # do not forget this. without this the object instance is same but init gets called on each retrieval from new  and last changes are gone


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, codes):
        self.__code = codes

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, texts):
        self.__text = texts

    def __repr__(self):
        print(f' this is a singleton instance')
        print(f' the object content is code : {self.__code} and text: {self.__text}')

