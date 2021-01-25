
# Stack  (Implementation: Partial)
# Queue (Implementation: Partial)
# BinarySearchTree (Implementation: Partial)
# AVL Tree (Implementation: Partial)

# Heaps (Implementation: Incomplete)
# Red Black Tree (Implementation: Incomplete)
# B Tree (Implementation: Incomplete)
# B+ Tree (Implementation: Incomplete)
# Graphs: Prims, Kruskals... (Implementation: Future Plan)




from avltree import AVLTree
from bst import BinarySearchTree
from treenode import TreeNode


# Testing Binary Search Tree Deletion

class MyTreeNode(TreeNode):
    value = 0
    def __init__(self, value):
        self.value = value

    def compare_to(self, object):
        if object.value < self.value:
            return 1
        if object.value > self.value :
            return -1
        return 0

    def __str__(self):
        return str(self.value)

avl = AVLTree()

def print_tree(avl):
    print("Inorder: ", [str(i) for i in avl.get_inorder_traversal()], " Postorder: ",
          [str(i) for i in avl.get_postorder_traversal()], avl.get_height())

avl.add(MyTreeNode(20))
print_tree(avl)
# avl.add(MyTreeNode(30))
# print_tree(avl)
# avl.add(MyTreeNode(35))
# print_tree(avl)
# avl.add(MyTreeNode(40))
# print_tree(avl)
# avl.add(MyTreeNode(41))
# print_tree(avl)
# avl.add(MyTreeNode(45))
# print_tree(avl)
# avl.add(MyTreeNode(46))
# print_tree(avl)
# avl.add(MyTreeNode(50))
# print_tree(avl)
# avl.add(MyTreeNode(60))
# print_tree(avl)
# avl.add(MyTreeNode(70))
# print_tree(avl)
# avl.add(MyTreeNode(42))
# print_tree(avl)

print(avl.remove(MyTreeNode(20)))
print_tree(avl)





