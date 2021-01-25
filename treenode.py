from abc import ABC


class TreeNode(ABC):
    # Abstract class to define a node of a Tree (This tree node will be used for binary search tree, avl trees and heaps )

    # Reference of the parent of this node
    parent = None

    # Reference of the left child of this node
    left_child = None

    # Reference of the right child of this node
    right_child = None

    # Holds height of tree
    height = 1

    def compare_to(self, object):
        # This method should be overridden in the child class
        # Abstract method to define the comparison between different TreeNode objects

        # Return 1 if current item is greater than object
        # Return 0 if current item is equal to object
        # Return -1 if current item is lesser than object
        pass