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
        size=self.countNodes()
        if (pos>=0 and pos<size):
            count=0
            cur=self.head
            while (cur!=None):
                if (count==pos):
                    return cur.info
                cur=cur.next
                count += 1
        else:
            return -999

    def addNodeAtPos(self, x, pos):
        size=self.countNodes()
        if (pos>=0 and pos<=size):
            if (pos==0):
                self.addFirst(x)
                return
            if (pos==size):
                self.addLast(x)
                return
            newNode=Node(x)
            count=0
            cur=self.head
            while (cur!=None):
                if (count+1==pos):                    
                    newNode.next=cur.next
                    cur.next=newNode
                    return
                cur=cur.next
                count+=1
        else:
            print(f"{pos} is out of range")
            
    def removeFirst(self):
        if (self.isEmpty()):
            return
        if (self.head.next is None):
            self.head=self.tail=None
            return
        self.head=self.head.next
    
    def removeLast(self):
        if (self.isEmpty()):
            return
        if (self.head.next is None):
            self.head=self.tail=None
            return 
        cur=self.head
        while (cur.next.next is not None):	#Move cur to infront of tail
            cur=cur.next
        self.tail=cur
        cur.next=None
    
    def removeNodeAtPos(self, pos):
        size=self.countNodes()
        if (pos>=0 and pos<size):
            if (pos==0):
                self.removeFirst()
                return
            if (pos==size-1):
                self.removeLast()
                return
            count=0;
            cur=self.head
            while (cur is not None):
                if (count+1==pos):
                    cur.next=cur.next.next
                    return
                cur=cur.next
                count += 1
        else:
             print(f"{pos} is out of range.")

    def addPrevious(self, x, pos):
        pass
    
    def addAfter(self, x, pos):
        pass
    
    def removePrevious(self, pos):
        pass

    def removeAfter(self, pos):
        pass 