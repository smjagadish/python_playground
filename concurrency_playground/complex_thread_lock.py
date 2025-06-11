import threading


class complex_task:
    def __init__(self):
        self._value = 0
        self.lock = threading.Lock()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,val):
        with self.lock:
          self._value = val

    def set_val(obj,val):
        print(f' thread currently executing is {threading.current_thread().native_id}')
        obj._value = val