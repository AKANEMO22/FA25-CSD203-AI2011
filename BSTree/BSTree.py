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