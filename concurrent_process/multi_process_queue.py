import time


class multi_task_queue():

    def __init__(self,*args,**kwargs):
        self.__id = kwargs['id']
        self.__region = kwargs['region']
        self.__inventory = kwargs['inventory']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,val):
        self.__id = val

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self,new_region):
        self.__region = new_region

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self,inv):
        if len(inv) == len(self.__inventory):
            self.__inventory = inv
        else:
            pass

    def add_element(self,val):
        time.sleep(1)
        self.__inventory.put(val)


    def get_element(self):
        time.sleep(3)
        print(self.__inventory.get())
