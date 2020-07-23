class Node:
    """
    Used to create the nodes for our linked list.
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """
        To append information at the end of the linked list.
        """
        new_node = Node()
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length_list(self):
        """
        Function to find the length of the linked list.
        """
        counter = 0
        cur = self.head
        while cur.next is not None:
            counter += 1
            cur = cur.next
        return counter

    def create_cycle(self, index):
        """
        Link the last node to an index in the linked list.
        """
        if index < 0 or index >= self.length_list()-1:
            print('ERROR: Index is invalid.')
            return
        cycle_node = None
        cur_ind = 0
        cur = self.head
        while cur.next is not None:
            if cur_ind == index:
                cycle_node = cur  # gets the node that is to be added
            cur = cur.next
            cur_ind += 1
        cur.next = cycle_node  # adds the node to the last one

    def has_cycle(self):
        """
        Checks whether there exists a cycle.
        """
        if not self.head.next:
            return False
        fast = self.head.next
        slow = self.head
        while fast is not None and fast.next is not None and slow is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


def main():
    """
    Debugging of the linkedlist class and algorithm.
    """
    llist = LinkedList()

    for i in range(1, 10):
        llist.append(i)

    print(llist.has_cycle())
    llist.create_cycle(4)
    print(llist.has_cycle())


if __name__ == '__main__':
    main()
