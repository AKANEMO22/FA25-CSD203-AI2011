from AVLTree import AVLTree
myAVL = AVLTree()
myAVL.root=myAVL.addAVLNode(myAVL.root, 44)
myAVL.root=myAVL.addAVLNode(myAVL.root, 17)
myAVL.root=myAVL.addAVLNode(myAVL.root, 78)
myAVL.root=myAVL.addAVLNode(myAVL.root, 32)
myAVL.root=myAVL.addAVLNode(myAVL.root, 50)
myAVL.root=myAVL.addAVLNode(myAVL.root, 88)
myAVL.root=myAVL.addAVLNode(myAVL.root, 48)
myAVL.root=myAVL.addAVLNode(myAVL.root, 62)
myAVL.root=myAVL.addAVLNode(myAVL.root, 54)

# myAVL.inOrder(myAVL.root)
myAVL.breadth_first_traversal()