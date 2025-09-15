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
    
    def getValueAtFirst(self):
        if (self.isEmpty()):
            print("The list is empty")
            return -999
        else:
            return self.head.info
    
    def getValueAtLast(self):
        if (self.isEmpty()):
            print("The list is empty")
            return -999
        else:
            return self.tail.info
    
    def addPrevious(self, x, pos):
        if (pos==0 or self.isEmpty()):
            self.addFirst(x)
            return
        size=self.countNodes()
        if (pos<0 or pos>size+1):
            return
        self.addNodeAtPos(x, pos-1)            
    
    def addAfter(self, x, pos):
        pass
    
    def removePrevious(self, pos):
        pass

    def removeAfter(self, pos):
        pass
    
    def getMaxValue(self):
        max=self.head.info
        cur=self.head
        while (cur is not None):
            if cur.info>max:
                max=cur.info
            cur=cur.next
        return max
    
    def getMinValue(self):
        min=self.head.info
        cur=self.head
        while (cur is not None):
            if cur.info<min:
                min=cur.info
            cur=cur.next
        return min        
        pass
    
    def getPosOfMaxTheK(self, k):
        max=self.getMaxValue()
        count=1; i=1; pos=-1
        cur=self.head
        while (cur is not None):
            if (cur.info==max):
                if (i==k):
                    pos=count
                    break
                else:
                    i+=1
            cur=cur.next
            count+=1
        return pos
    
    def getPosOfMinTheK(self, k):
        min=self.getMinValue()
        count=1; i=1; pos=-1
        cur=self.head
        while (cur is not None):
            if (cur.info==min):
                if (i==k):
                    pos=count
                    break
                else:
                    i+=1
            cur=cur.next
            count+=1
        return pos
        pass
    #Bubble sort
    def SortListAsc(self):
        cur=self.head
        while cur.next:
            p=cur.next
            while p:
                if cur.info>p.info:		#switch ASC <=> DESC
                    temp=cur.info; cur.info=p.info; p.info=temp
                p=p.next
            cur=cur.next            
    
    def SortListDesc(self):
        cur=self.head
        while cur.next:
            p=cur.next
            while p:
                if cur.info<p.info:		#switch ASC <=> DESC
                    temp=cur.info; cur.info=p.info; p.info=temp
                p=p.next
            cur=cur.next
            
    #Return position of node(x).
    #Return -1 in case find not found
    def getPosOfNode(self, x):
        pass
    
    def SortListAscPos1toPos2(self,pos1,pos2):
        pass
    
    def removeAllNode(self, x):
        pass
    
    