from Node import Node
class Stack:
    def __init__(self):
        self.head=None
        pass
    
    def isEmpty(self):
        return self.head==None
    
    def push(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=newNode
            return
        newNode.next=self.head
        self.head=newNode
    
    def pop(self):
        if self.isEmpty():
            print("error")
            return
        x=self.head.info
        if self.head.next is None:
            self.head=None
            return x
        self.head=self.head.next
        return x        
    
    def top(self):
        if self.isEmpty():
            print("error")
            return
        return self.head.info
    
    def len(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count            
