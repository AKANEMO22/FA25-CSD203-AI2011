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
print()
myAVL.root=myAVL.deleteByCopyingLeft(myAVL.root,62)
myAVL.root=myAVL.deleteByCopyingLeft(myAVL.root,54)
myAVL.root=myAVL.deleteByCopyingLeft(myAVL.root,50)
myAVL.breadth_first_traversal()
# 44 17 78 32 50 88 48 62
# 44 17 62 32 50 78 48 54 88 