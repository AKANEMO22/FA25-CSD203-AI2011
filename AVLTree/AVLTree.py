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

    #Find the maximum of the left subtree
    def findRightMostNode(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node     
    
    #Find the copy node at the left subtree
    def deleteByCopyingLeft1(self, node, x):
        if node is None:
            print(f"Find not found {x}")
            return
        if x<node.info:
            node.left=self.deleteByCopyingLeft(node.left,x)
        elif x>node.info:
            node.right=self.deleteByCopyingLeft(node.right,x)
        else:
            #Only has a right child
            if node.left is None:
                return node.right
            #Only has a left child
            if node.right is None:
                return node.left
            nodeCopy=self.findRightMostNode(node.left)
            node.info=nodeCopy.info
            node.left=self.deleteByCopyingLeft(node.left, nodeCopy.info)
        node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
        balanceFactor=self.getBalance(node)
       
        if balanceFactor>1:
            #Case 1
            if node.left and x < node.left.info:
                return self.rightRotation(node)        
            #Case 2
            elif node.left:
                if x > node.left.info:
                    node.left=self.leftRotation(node.left)
                return self.rightRotation(node)
        if balanceFactor<-1:
        #Case 3
            if node.right and x > node.right.info:
                return self.leftRotation(node)        
            #Case 4
            elif node.right:
                if x < node.right.info:
                    node.right=self.rightRotation(node.right)
                return self.leftRotation(node)
#         node.height=max(self.getHeight(node.left), self.getHeight(node.right))+1
        return node
    
    def deleteByCopyingLeft(self, node, x):
        if node is None:
            print(f"Node {x} not found.")
            return None

        if x < node.info:
            node.left = self.deleteByCopyingLeft(node.left, x)
        elif x > node.info:
            node.right = self.deleteByCopyingLeft(node.right, x)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                nodeCopy = self.findRightMostNode(node.left)
                node.info = nodeCopy.info
                node.left = self.deleteByCopyingLeft(node.left, nodeCopy.info)

        # Update height
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

        # Rebalance
        balance = self.getBalance(node)

        # Left heavy
        if balance > 1:
            if node.left and self.getBalance(node.left) >= 0:
                return self.rightRotation(node)
            elif node.left:
                node.left = self.leftRotation(node.left)
                return self.rightRotation(node)

        # Right heavy
        if balance < -1:
            if node.right and self.getBalance(node.right) <= 0:
                return self.leftRotation(node)
            elif node.right:
                node.right = self.rightRotation(node.right)
                return self.leftRotation(node)

        return node

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