

class BinarySearchTree:
    # Class to Implement the Binary Search Tree Data Structure
    # Note: The nodes of this tree will have to inherit TreeNode class because it is the interface for the Nodes of this Tree

    # Root of the Tree
    root = None

    def add(self, *nodes):

        # Adds Multiple number of nodes  in the Binary Search Tree one by one
        # Parameters:
        #   nodes: The variable number of nodes to insert in the Tree. Each node has to inherit TreeNode

        # If some node is already present, it will not be added to the tree.
        # The function will terminate normally. No Exceptions will be raised.

        for node in nodes:
            self._add_node(node)

    def _add_node(self, node):
        # Adds one node to the BST

        if self.root is None:
            self.root = node
        else:

            # BST node insertion
            current_node = self.root
            while (True):
                if current_node.compare_to(node) < 0:
                    if current_node.right_child is None:
                        current_node.right_child = node
                        node.parent = current_node
                        break
                    else:
                        current_node = current_node.right_child
                elif current_node.compare_to(node) > 0:
                    if current_node.left_child is None:
                        current_node.left_child = node
                        node.parent = current_node
                        break
                    else:
                        current_node = current_node.left_child
                else:
                    break

            # Height calculation
            current_node = node.parent
            while current_node is not None:
                current_node.height = self._calculate_height(current_node)
                current_node = current_node.parent

    def search(self, key):

        # Searches for the key in the Tree
        # Paramters:
        #   key: This is node which is to be searched in the Tree. It has to inherit TreeNode class
        # Returns: True if node is present otherwise false

        current_node = self.root
        while current_node is not None:
            if current_node.compare_to(key) < 0:
                current_node = current_node.right_child
            elif current_node.compare_to(key) > 0:
                current_node = current_node.left_child
            else:
                return True

        return False

    def get_inorder_traversal(self):

        # Returns a list of nodes containing the inorder traversal of tree

        def inorder(root):
            if root is not None:
                left = []
                right = []
                if root.left_child is not None:
                    left = [*inorder(root.left_child)]
                if root.right_child is not None:
                    right = [*inorder(root.right_child)]
                return [*left, root, *right]
            return []

        return inorder(self.root)

    def get_postorder_traversal(self):

        # Returns a list of nodes containing the postorder traversal of the tree

        def postorder(root):
            if root is not None:
                left = []
                right = []
                if root.left_child is not None:
                    left = [*postorder(root.left_child)]
                if root.right_child is not None:
                    right = [*postorder(root.right_child)]
                return [*left, *right, root]
            return []

        return postorder(self.root)

    def get_preorder_traversal(self):
        # Returns a list of nodes containing the preorder traversal of the tree
        def preorder(root):
            if root is not None:
                left = []
                right = []
                if root.left_child is not None:
                    left = [*preorder(root.left_child)]
                if root.right_child is not None:
                    right = [*preorder(root.right_child)]
                return [root, *left, *right]
            return []
        return preorder(self.root)

    def get_height(self):
        if self.root is None:
            return 0
        return self.root.height

    def _calculate_height(self, current_node):
        # Calculates the height of the tree from the current node using the left and the right children's heights

        if current_node.left_child is None:
            if current_node.right_child is None:
                return 1
            return 1 + current_node.right_child.height
        elif current_node.right_child is None:
            if current_node.left_child is None:
                return 1
            return 1 + current_node.left_child.height

        return 1 + max(current_node.left_child.height, current_node.right_child.height)

    def remove(self, node):

        # Removes the node from the Tree

        # Returns:  True: If node removal was successful
        #           False: If node was not found in the tree


        current_node = self.root
        while current_node is not None:
            if current_node.compare_to(node) < 0:
                current_node = current_node.right_child
            elif current_node.compare_to(node) > 0:
                current_node = current_node.left_child
            else:
                self._delete(current_node)
                return True
        return False

    def _delete(self, node):

        # Deletes the node from the Tree

        # Holds the node to delete
        b = node

        # Parent of the node to delete (Can be None if b is the root)
        a = b.parent

        # Holds the parent of the First Node of the Inorder Traversal of the right subtree of b
        d = None

        if b.right_child is not None:

            # If the right subtree of the node is present, we need to find the first node of that subtree's inorder traversal

            # Holds root of the right subtree of b
            c = b.right_child

            # Holds the first node of that subtree's inorder traversal (It can be equal to c if the right subtree consists of only one node)
            e = self._find_inorder_first_node(c)

            # If a does not exist, b is the root of this tree which is to be deleted
            if a is not None:

                if a.left_child is not None:
                    if a.left_child.compare_to(b) == 0:
                        # If left child of a is b, make e the left child of a

                        a.left_child = e
                    else:
                        # If right child of a is b, make e the right child of a

                        a.right_child = e
                else:
                    a.right_child = e
            else:
                # If a is None, make e the root of the tree

                self.root = e

            # If b has left child, make it the left child of e
            if b.left_child is not None:
                e.left_child = b.left_child
                b.left_child.parent = e


            if e.compare_to(c)!=0:

                # If e is not equal to c, d is parent of e

                d = e.parent

                # If right child of e exists, make it the left child of d. Else make left child of d to be None
                if e.right_child is not None:
                    d.left_child = e.right_child
                    e.right_child.parent = d
                else:
                    e.parent.left_child = None

                # Make c the right child of e
                e.right_child = c
                c.parent = e
            else:
                # If e is equal to c, make d to be c
                d = c

            e.parent = a
        else:
            # If the right child of b does not exist, then there is no problem


            if b.left_child is not None:
                # If the left child of b does not exist, make the appropriate child of a (which was holding b) to be None

                b.left_child.parent = a
                if a is not None:
                    if a.left_child is not None:
                        if a.left_child.compare_to(b) == 0:
                            a.left_child = b.left_child
                        else:
                            a.right_child = b.left_child
                    else:
                        a.right_child = b.left_child
                else:
                    # If a is None, then make the left child of b to be the root because b was itself the root
                    self.root = b.left_child
            else:
                # If both the children of b are None, make the root none if a is none otherwise make it None(left child of b is also none)

                if a is not None:
                    if a.left_child is not None:
                        if a.left_child.compare_to(b) == 0:
                            a.left_child = b.left_child
                        else:
                            a.right_child = b.left_child
                    else:
                        a.right_child = b.left_child
                else:
                    self.root = None
        # Height Calculation : Use d to re-calculate the heights of the nodes.
        current_node = d
        while current_node is not None:
            current_node.height = self._calculate_height(current_node)
            current_node = current_node.parent

        del b

    def _find_inorder_first_node(self, node):
        # Calculates the first node of the inorder traversal with "node" as the root

        current_node = node
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def is_empty(self):
        return self.root is None