from bst import BinarySearchTree

class AVLTree(BinarySearchTree):
    # Implementation of AVL Trees which are self height balanced. It optimizes search time
    # Note: The nodes of this tree will have to inherit TreeNode class because it is the interface for the Nodes of this Tree

    # TODO: Delete functionality


    def add(self, *nodes):
        # Adds Multiple number of nodes  in the AVL Tree one by one
        # Parameters:
        #   nodes: The variable number of nodes to insert in the Tree. Each node has to inherit TreeNode

        # If some node is already present, it will not be added to the tree.
        # The function will terminate normally. No Exceptions will be raised.


        for node in nodes:
            self._add_node(node)


    def _add_node(self, node):

        # Adds one node to the AVLTree

        if self.root is None:
            self.root=node

        else:

            # Normal Binary Search Tree Insertion
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

            # AVL Tree height Balancing
            current_node = node.parent

            while current_node is not None:

                current_node.height = self._calculate_height(current_node)
                balance_factor = self.__calculate_balance_factor(current_node)

                if (balance_factor>1 and current_node.left_child.compare_to(node)>0):
                    self.__left_left_rotation(current_node)

                elif (balance_factor>1 and current_node.left_child.compare_to(node)<0):
                    self.__left_right_rotation(current_node)

                elif (balance_factor<-1 and current_node.right_child.compare_to(node)>0):
                    self.__right_left_rotation(current_node)

                elif (balance_factor<-1 and current_node.right_child.compare_to(node)<0):
                    self.__right_right_rotation(current_node)

                current_node = current_node.parent

            while self.root.parent is not None:
                self.root = self.root.parent

    def __left_left_rotation(self, node):

        a = node
        b = node.left_child
        if a.parent is not None:
            if a.parent.right_child is not None:
                if a.parent.right_child.compare_to(a) == 0:
                    a.parent.right_child = b
            if a.parent.left_child is not None:
                if a.parent.left_child.compare_to(a) == 0:
                    a.parent.left_child = b

        b.parent = a.parent
        a.parent = b
        if b.right_child is not None:
            a.left_child = b.right_child
            a.left_child.parent = a
        else:
            a.left_child = None

        b.right_child = a
        a.height -=2


    def __left_right_rotation(self, node):
        a = node
        b = node.left_child
        c = node.left_child.right_child

        if a.parent is not None:
            if a.parent.right_child is not None:
                if a.parent.right_child.compare_to(a) == 0:
                    a.parent.right_child = c
            if a.parent.left_child is not None:
                if a.parent.left_child.compare_to(a) == 0:
                    a.parent.left_child = c

        c.parent = a.parent
        b.parent = c

        if c.left_child is not None:
            b.right_child = c.left_child
            c.left_child.parent = b

        else:
            b.right_child = None
        c.left_child = b

        if c.right_child is not None:
            a.left_child = c.right_child
            c.right_child.parent = a

        else:
            a.left_child = None
        c.right_child = a
        a.parent = c

        c.height +=1
        b.height -=1
        a.height -=2

    def __right_right_rotation(self, node):
        a = node
        b = node.right_child

        if a.parent is not None:
            if a.parent.right_child is not None:
                if a.parent.right_child.compare_to(a) == 0:
                    a.parent.right_child = b
            if a.parent.left_child is not None:
                if a.parent.left_child.compare_to(a) == 0:
                    a.parent.left_child = b

        b.parent = a.parent
        a.parent = b

        if b.left_child is not None:
            a.right_child = b.left_child
            a.right_child.parent = a

        else:
            a.right_child = None
        b.left_child = a
        a.height -=2

    def __right_left_rotation(self, node):

        a = node
        b = node.right_child
        c = node.right_child.left_child

        if a.parent is not None:
            if a.parent.right_child is not None:
                if a.parent.right_child.compare_to(a) == 0:
                    a.parent.right_child = c
            if a.parent.left_child is not None:
                if a.parent.left_child.compare_to(a) == 0:
                    a.parent.left_child = c

        c.parent = a.parent
        a.parent = c

        if c.left_child is not None:
            a.right_child = c.left_child
            c.left_child.parent = a

        else:
            a.right_child = None
        c.left_child = a

        if c.right_child is not None:
            b.left_child = c.right_child
            c.right_child.parent = b

        else:
            b.left_child = None
        c.right_child = b
        b.parent = c

        c.height +=1
        b.height -=1
        a.height -=2

    def __calculate_balance_factor(self, current_node):

        # Calculates balance factor for a particular node by taking into account
        # the heights of the left subtree and right subtree

        if current_node.left_child is None:
            if current_node.right_child is None:
                return 0
            return -current_node.right_child.height
        if current_node.right_child is None:
            if current_node.left_child is None:
                return 0
            return current_node.left_child.height

        return current_node.left_child.height - current_node.right_child.height

