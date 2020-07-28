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
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        """
        If the current index has a right child.
        """
        return self.get_right_child_index(index) < len(self.heap)

    def has_parent(self, index):
        """
        If the current index has a parent.
        """
        return self.get_parent_index(index) < len(self.heap)

    def get_left_child(self, index):
        """
        Gets the value of the left child.
        """
        return self.heap[self.get_left_child_index(index)]

    def get_right_child(self, index):
        """
        Gets the value of the right child.
        """
        return self.heap[self.get_right_child_index(index)]

    def get_parent(self, index):
        """
        Gets the value of the parent.
        """
        return self.heap[self.get_parent_index(index)]

    def swap_values(self, index1, index2):
        """
        Swaps the values at 2 given indices.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def peek(self):
        """
        Returns the root i.e the min element of the array.
        """
        assert len(self.heap) > 0, "ERROR: Heap is empty."
        return self.heap[0]

    def poll(self):
        """
        Removes the root i.e the min element from the array.
        """
        assert len(self.heap) > 0, "ERROR: Heap is empty."
        item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return item

    def add(self, value):
        """
        Adds an element to the end of the heap and then fixes the heap.
        """
        self.heap.append(value)
        self.heapify_up()

    def heapify_up(self):
        """
        Start with the last element and walk up the heap and swap in case the
        elements are out of order.
        """
        index = len(self.heap) - 1
        while self.has_parent(index) and self.get_parent(index) > self.heap[index]:
            self.swap_values(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        """
        Start with the root element and keep walking down and fixing the heap
        while there are children.
        """
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap_values(index, smaller_child_index)
            index = smaller_child_index


def main():
    """
    Tests the min heap class.
    """
    heap = MinHeap()
    for i in range(10):
        heap.add(i)
    print(heap.peek())
    for i in range(4):
        heap.poll()
    print(heap.peek())


if __name__ == '__main__':
    main()
