from Car import Car
from Node import Node
class SinglyLinkedListObj:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def isEmpty(self):
        return self.head==None
    
    def addFirst(self, _id, _name, _price):
        x=Car(_id, _name, _price)
        newNode = Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        cur=self.head
        print(f"{'ID':<5} {'Name':<25} {'Price':^9}")
        print(f"{'--':<5} {'----':<25} {'-----':^9}")
        while cur:
            print(cur.info)
            cur=cur.next
            