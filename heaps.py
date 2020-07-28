class MinHeap:
    def __init__(self):
        """
        Initialises the min heap as an array.
        """
        self.heap = []

    def get_left_child_index(self, parent):
        """
        Gets the index position of the left child of the current index.
        """
        return 2*parent+1

    def get_right_child_index(self, parent):
        """
        Gets the index position of the right child of the current index.
        """
        return 2*parent+2

    def get_parent_index(self, child):
        """
        Returns the index position of the parent index for a given child index.
        """
        return (child-1)//2

    def has_left_child(self, index):
        """
        If the current index has a left child.
        """
        return get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        """
        If the current index has a right child.
        """
        return get_right_child_index(index) < len(self.heap)

    def has_parent(self, index):
        """
        If the current index has a parent.
        """
        return get_parent_index(index) < len(self.heap)

    def get_left_child(self, index):
        """
        Gets the value of the left child.
        """
        return self.heap[get_left_child_index(index)]

    def get_right_child(self, index):
        """
        Gets the value of the right child.
        """
        return self.heap[get_right_child_index(index)]

    def get_parent(self, index):
        """
        Gets the value of the parent.
        """
        return self.heap[get_parent_index(index))]

    def swap_values(self, index1, index2):
        """
        Swaps the values at 2 given indices.
        """
        self.heap[index1], self.heap[index2]=self.heap[index2], self.heap[index1]

    def peek(self):
        """
        Returns the root i.e the min element of the array.
        """
