from linkedlist import linkedlist
class linkedlistHelper():
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        obj = linkedlist()
        obj.data = data
        if self.head is None:
            self.head = obj
            obj.next = None
            self.tail = obj
        else:
            self.tail.next = obj
            obj.next = None
            self.tail = obj

    def printnodes(self):
        obj = self.head
        if self.head == self.tail:
            print(f'node content:{obj.data}->',end='')
        while obj.next is not None:
            print(f'node content:{obj.data}->',end='')
            obj = obj.next
        print(f'node content:{self.tail.data}')

    def insertafter(self,data,after):
        print(f' will insert node with value :{data} after node with value :{after}')
        obj = self.head
        while after != obj.data:
            obj = obj.next
        new_obj = linkedlist()
        new_obj.data = data
        if obj == self.tail:
            new_obj.next = None
            obj.next = new_obj
            self.tail = new_obj
        else:
            new_obj.next = obj.next
            obj.next = new_obj

    def countnodes(self):
        count = 0
        obj = self.head
        while(obj.next is not None):
            count+=1
            obj = obj.next
        print(f'the total count of nodes in the linked list ts {count+1}')

    def deletenode(self,value):
        print(f'deleting the node with first occurence of data:{value}')
        obj = self.head
        if value == obj.data:
            self.head = obj.next
            return
        while obj.next is not None and value != obj.next.data:
            obj = obj.next
        if obj.next.next is not None:
          obj.next = obj.next.next
        else:
            obj.next = None
            self.tail = obj

    def trigger(self):
        print(f'reversing the linked list through recursion')
        self.reversenodes(self.head)

    def reversenodes(self,obj):
        '''
         this function will reverse the contents of a linked list
         1->2->3->4 becomes 4->3->2->1
          2 , 3 , 4
        :return:
        '''
        fn_obj = obj

        while obj.next is not None:
            obj = obj.next
            self.reversenodes(obj)

        if fn_obj == self.tail:
            self.head = fn_obj
            #obj.next = None
        else:

            obj.next = fn_obj
            fn_obj.next = None
            self.tail = fn_obj



















