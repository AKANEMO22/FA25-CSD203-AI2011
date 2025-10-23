from Node import Node
from Queue import Queue
class AVLTree:
    def __init__(self, root=None):
        self.root=None if root is None else Node(root)
        
    def isEmpty(self):
        return self.root==None
    
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height
    
    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)
        
    def rightRotation(self, node):
        k=node.left
        node.left=k.right
        k.right=node
        node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
        k.height=max(self.getHeight(k.left), self.getHeight(k.right))+1
        return k

    def leftRotation(self, node):
        k=node.right
        node.right=k.left
        k.left=node
        node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
        k.height=max(self.getHeight(k.left), self.getHeight(k.right))+1
        return k
    
    def addAVLNode(self, node, x):
        if node is None:
            return Node(x)
        if x < node.info:
            node.left=self.addAVLNode(node.left, x)
        elif x > node.info:
            node.right=self.addAVLNode(node.right, x)
        else:
            return node
        node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
        balanceFactor=self.getBalance(node)
        #Case 1
        if balanceFactor>1 and x < node.left.info:
            return self.rightRotation(node)        
        #Case 2
        if balanceFactor>1 and x > node.left.info:
            node.left=self.leftRotation(node.left)
            return self.rightRotation(node)
        #Case 3
        if balanceFactor<-1 and x > node.right.info:
            return self.leftRotation(node)        
        #Case 4
        if balanceFactor<-1 and x < node.right.info:
            node.right=self.rightRotation(node.right)
            return self.leftRotation(node)
        return node
    
    def inOrder(self, root):
        if root is None:
            return
        if root.left is not None:
            self.inOrder(root.left)
        print(root.info,end=' ')	#Visit root
        if root.right is not None:
            self.inOrder(root.right)

    def visit(self, v):
        if v is None:
            return
        print(v.info,end=' ')
        
    def breadth_first_traversal(self):
        if self.isEmpty():
            return
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            self.visit(p)
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)            