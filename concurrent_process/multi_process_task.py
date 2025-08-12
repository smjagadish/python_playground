from typing import List
class process_task:
    def __init__(self,*args,**kwargs):
        self.__id:int = kwargs['id']
        self.__name:str = kwargs['task_name']
        self.__tlist:List[int] = kwargs['task_list']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,val):
        self.__id = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def tlist(self):
        return self.__tlist

    @tlist.setter
    def tlist(self,new_list):
        if len(self.__tlist) == len(new_list):
            self.__tlist = new_list
        else:
            pass

    def add_tlist(self,data):
        self.__tlist.append(data)
