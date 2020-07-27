class BSTNode:
    def __init__(self, data):
        """
        Initialises each node of a BST with some left node, right node and some
        user inputted data.
        """
        self.data = data
        self.left = None
        self.right = None
        self.l_bst, self.r_bst = True, True

    def add_child(self, data):
        """
        Add a child node with some value, checks where in the tree it fits and
        if the value is unique.
        """
        if data == self.data:  # value already exists
            return
        if data < self.data:  # append it to the left sub-tree
            if self.left:  # recursive call until you find a leaf node
                self.left.add_child(data)
            else:  # leaf tree
                self.left = BSTNode(data)
        else:  # add it to the right sub-tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def in_order_traversal(self):
        """
        Walk the tree and return elements in the order -> left sub-tree followed
        by root followed by right sub-tree.
        """
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)  # root node

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        """
        Search for a value in the BST in O(log(n)) time.
        """
        if value == self.data:
            return True

        if value < self.data:  # value might be in left sub-tree.
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:  # value might be in right sub-tree.
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        """
        Finds maximum element in subtree.
        """
        if not self.right:
            return self.data
        return self.right.find_max()

    def find_min(self):
        """
        Finds the minimum value in subtree.
        """
        if not self.left:
            return self.data
        return self.left.find_min()

    def delete(self, value):
        """
        Deletes a particular node from the binary search tree.
        """
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:  # value is found
            if self.left is None and self.right is None:  # only a leaf node.
                return None
            if self.left is None:  # parent with one child
                return self.right
            if self.right is None:  # parent with one child
                return self.left

            """
            One of 2 methods to balance the binary tree after the deletion.
            """
            # METHOD 1
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            # METHOD 2
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def check_bst(self, min, max):
        """
        Checks whether a given tree is a binary search tree by comparing its
        values to some bounds.
        """
        if self is None:
            return True
        if not min < self.data < max:
            return False
        if self.left:
            self.l_bst = self.left.check_bst(min, self.data)
        if self.right:
            self.r_bst = self.right.check_bst(self.data, max)
        return self.l_bst and self.r_bst


def main(elems):
    """
    Builds a tree based on a list of numbers and then checks to see whether the
    class BSTNode works.
    """
    root = BSTNode(elems[0])
    for elem in elems[1:]:
        root.add_child(elem)

    print(root.in_order_traversal())
    print(root.search(32))
    root.delete(32)
    print(root.in_order_traversal())
    print(root.check_bst(float('-inf'), float("inf")))


if __name__ == '__main__':
    nums = [4, 6, 5, 2, 1, 3, 78, 32, 51, 13, 14]
    main(nums)
