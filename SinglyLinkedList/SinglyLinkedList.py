from Node import Node
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def isEmpty(self):
        return self.head==None
    
    def addFirst(self, x):
        newNode=Node(x)
        if (self.isEmpty()):
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        pass
    
    def display(self):
        cur=self.head
        while (cur is not None):
            print(cur.info, end=" ")
            cur=cur.next
        print()
        
    def addLast(self, x):
        newNode=Node(x)
        if (self.isEmpty()):
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        
    def countNodes(self):
        count=0
        cur=self.head
        while (cur is not None):
            count+=1
            cur=cur.next
        return count
    
    def getValueAtPos(self, pos):
        pass
    
    def addNodeAtPos(self, x, pos):
        pass
    
    def removeFirst(self):
        pass
    
    def removeLast(self):
        pass
    
    def removeNodeAtPos(self, pos):
        pass
        