from Node import Node
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        pass
    
    def isEmpty(self):
        return self.head==None
    
    def enqueue(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
            return
        self.tail.next=newNode
        self.tail=newNode

    #Get value at the begining then remove it.
    def dequeue(self):
        if self.isEmpty():
            print("error.")
            return
        x=self.head.info
        if self.head.next is None:            
            self.head=self.tail=None
            return x        
        self.head=self.head.next
        return x
    
    #Get value at the beginning without remove
    def first(self):
        if self.isEmpty():
            print("error.")
            return
        return self.head.info        

    def len(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count    
        

