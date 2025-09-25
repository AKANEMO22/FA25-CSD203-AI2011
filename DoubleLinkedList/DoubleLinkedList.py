from Node import Node
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return self.head==None
    
    def addFirst(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
            return
        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode
    
    def display(self):
        cur=self.head
        while cur:
            print(cur.info, end=' ')
            cur=cur.next
#         print("\n")
        
    def countNode(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count
    
    def addLast(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    
    def removeFirst(self):
        if self.isEmpty():
            return
        if self.head.next is None:
            self.head=self.tail=None
            return        
        self.head.next.prev=None
        self.head=self.head.next
    
    def removeLast(self):
        if self.isEmpty():
            return
        if self.head.next is None:
            self.head=self.tail=None
            return
        self.tail.prev.next=None
        self.tail=self.tail.prev
    
    def addAtPost(self, x, pos):
        n=self.countNode()
        if (pos<0 or pos>n):
            print(f"{pos} is out of range")
            return
        if pos==0:
            self.addFirst(x)
            return
        if pos==n:
            self.addLast(x)
            return
        cur=self.head
        i=0
        while i!=pos:		#Move cur to pos
            cur=cur.next
            i+=1
        newNode=Node(x)
        cur.prev.next=newNode
        newNode.prev=cur.prev
        cur.prev=newNode
        newNode.next=cur        
    
    def removeAtPos(self, pos):
        n=self.countNode()
        if (pos<0 or pos>=n):
            print(f"{pos} is out of range")
            return
        if pos==0:
            self.removeFirst()
            return
        if pos==n-1:
            self.removeLast()
            return
        cur=self.head
        i=0
        while i!=pos:	#Move cur to pos
            cur=cur.next
            i+=1        
        cur.prev.next=cur.next
        cur.next.prev=cur.prev        
#     Bubble sort    
    def sortListAsc(self):
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info>q.info:		#Sort ASC <=> DESC by changing > to < 
                    t=cur.info; cur.info=q.info; q.info=t
                q=q.next
            cur=cur.next
        pass
    
    def sortListDesc(self):
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info<q.info:		#Sort ASC <=> DESC by changing > to < 
                    t=cur.info; cur.info=q.info; q.info=t
                q=q.next
            cur=cur.next        
        pass
    
    def editNodeAtPos(self, x, pos):
        pass
    
    def getValueAtPos(self, pos):
        pass