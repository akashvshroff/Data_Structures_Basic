class MinHeap:
    def __init__(self):
        """
        Initialises the min heap as an array.
        """
        self.heap = []

    def get_left_child(self, parent):
        """
        Gets the index position of the left child of the current index.
        """
        return 2*parent+1

    def get_right_child(self, parent):
        """
        Gets the index position of the right child of the current index.
        """
        return 2*parent+2

    def get_parent(self, child):
        """
        Returns the index position of the parent index for a given child index.
        """
        return (child-1)//2
