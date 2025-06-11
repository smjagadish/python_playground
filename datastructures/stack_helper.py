from stack_class import stack_impl
class stackhelper():
    def __init__(self):
        self.top = None
        self.count = 0
        self.head = None

    def getstackcapacity(self):
        return stack_impl.capacity

    def pushElement(self,data):
        if self.count <= self.getstackcapacity():
            obj = stack_impl()
            obj.data = data
            print(f'added stack element with value{data}')
            if self.count == 0:
                obj.next = None
                self.top = obj
                self.head = obj
                self.count+=1
            else:
                self.top.next = obj
                obj.next = None
                self.top = obj
                self.count+=1
        else:
            raise Exception('the stack is full , retry later')




    def popElement(self):
        if self.count == 0:
            raise Exception('there is no element in the stack to pop , retry after some time')
        else:
            obj = self.head
            if obj == self.top:
                self.count -=1
                print(f'removed stack element with value:{self.top.data}')
                return
            while obj.next!=self.top:
                obj = obj.next
            print(f'removed stack element with value:{self.top.data}')
            self.top = obj
            self.count-=1
    def peekElement(self):
        if self.count == 0:
            raise Exception('there is no element in stack to peek , retry after some time')
        else:
            print(f'peeking top of stack:{self.top.data}')



