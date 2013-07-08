"""
Binary Search Tree Implementation
@jlengrand
2013/07
"""


class BinarySearchTree():
    """
    Defines a complete binary search Tree.
    A binary search tree has a root node.
    We also add a size to the search tree, that corresponds to the number of
    nodes it has.
    """
    def __init__(self):
        self.size = 0
        self.root_node = None

    def add(self, value):
        """
        Adds the input value in the right position of the binary search Tree
        The rule is, left children of a node have a value < than the value
        of the node.
        Right children of a node conversely have a value >= of the value of
        the node.
        """
        if self.size == 0:
            self.root_node = BinarySearchNode(value, None)  # root node has no parent

        else:
            node = self.root_node
            is_left = None
            while(node is not None):
                ptr_node = node  # keep parent in memory
                if node.value > value:  # we go to the left child
                    node = node.left_child
                    is_left = True
                else:  # we move to the right child. This means = case too
                    node = node.right_child
                    is_left = False

            # we reached a leaf
            node = BinarySearchNode(value, ptr_node)
            if is_left:
                ptr_node.left_child = node
            else:
                ptr_node.right_child = node

        self.size += 1

    def max(self):
        """
        Returns the highest node value of the tree.
        Otherwise, returns None
        """
        if self.size == 0:
            return None
        else:  # we have nodes in the tree
            node = self.root_node
            while(node.has_right_child()):
                node = node.right_child

            # we have the leaf
            return node.value

    def min(self):
        """
        Returns the lowest node value of the tree.
        Otherwise returns None
        """
        if self.size == 0:
            return None
        else:  # we have nodes in the tree
            node = self.root_node
            while(node.has_left_child()):
                node = node.left_child

            # we have the leaf
            return node.value


class BinarySearchNode():
    """
    Defines any node of the Binary Search Tree.
    A node has at most 2 children, and it has a value.
    It also must have a parent
    """
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value

        self.left_child = None
        self.right_child = None

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None
