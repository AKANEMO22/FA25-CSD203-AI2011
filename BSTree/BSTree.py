from Queue import Queue
from Node import Node
class BSTree:
    def __init__(self, root=None):
        self.root=None if root is None else Node(root)
        pass
    
    def isEmpty(self):
        return self.root==None
    
    def addTreeNode(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.root=newNode
            return
        cur=self.root
        while cur:
            if cur.info==newNode.info:
                print(f"{x} is already existing in the tree.")
                return
            if newNode.info < cur.info:
                if cur.left is None:
                    cur.left=newNode
                    return
                else:
                    cur=cur.left
            else:
                if cur.right is None:
                    cur.right=newNode
                    return
                else:
                    cur=cur.right

    def preOrder(self, root):
        if root is None:
            return
        print(root.info,end=' ') 	#Visit root
        if root.left is not None:
            self.preOrder(root.left)        
        if root.right is not None:
            self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        if root.left is not None:
            self.inOrder(root.left)
        print(root.info,end=' ')	#Visit root
        if root.right is not None:
            self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        if root.left is not None:
            self.postOrder(root.left)        
        if root.right is not None:
            self.postOrder(root.right)
        print(root.info,end=' ')	#Visit root
        
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
              
    def countNodeHasTwoChildren(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is not None and p.right is not None:
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)
        return count
    
    def countNodesHasOnlyLeftChild(self, root):
        if root is None:
            return 0
        count=l=r= 0
        if root.left is not None:
            l=self.countNodesHasOnlyLeftChild(root.left)
        if root.left is not None and root.right is None:            
            count+=1
        if root.right is not None:
            r=self.countNodesHasOnlyLeftChild(root.right)        
        return l+count+r
    
    def countNodesHasOnlyRightChild(self, root):
        if root is None:
            return 0
        count=l=r= 0
        if root.left is not None:
            l=self.countNodesHasOnlyRightChild(root.left)
        if root.left is None and root.right is not None:            
            count+=1
        if root.right is not None:
            r=self.countNodesHasOnlyRightChild(root.right)        
        return l+count+r
    
    def countNodesWithValueGreaterThanX(self, root, x):
        if root is None:
            return 0
        count=l=r= 0
        if root.left is not None:
            l=self.countNodesWithValueGreaterThanX(root.left, x)
        if root.info>x:        
            count+=1
        if root.right is not None:
            r=self.countNodesWithValueGreaterThanX(root.right, x)        
        return l+count+r        
        pass
    
    #Find the minimum of the right subtree
    def findLeftMostNode(self, node):
        if self.root is None:
            return None
        p=node.right
        while p.left:
            p=p.left
        return p    
   
    #Find the maximum of the left subtree
    def findRightMostNode(self, node):
        if node is None:
            return None
        p=node.left
        while p.right:
            p=p.right
        return p        
    
    #Find the copy node at the left subtree
    def deleteByCopyingLeft(self, node, x):
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
            nodeCopy=self.findRightMostNode(node)
            node.info=nodeCopy.info
            node.left=self.deleteByCopyingLeft(node.left, nodeCopy.info)            
        return node
     
     #Find the copy node at the right subtree 
    #Find the copy node at the left subtree
    def deleteByCopyingRight(self, node, x):
        if node is None:
            print(f"Find not found {x}")
            return
        if x<node.info:
            node.left=self.deleteByCopyingRight(node.left,x)
        elif x>node.info:
            node.right=self.deleteByCopyingRight(node.right,x)
        else:
            #Only has a right child
            if node.left is None:
                return node.right
            #Only has a left child
            if node.right is None:
                return node.left
            nodeCopy=self.findLeftMostNode(node)
            node.info=nodeCopy.info
            node.right=self.deleteByCopyingRight(node.right, nodeCopy.info)            
        return node