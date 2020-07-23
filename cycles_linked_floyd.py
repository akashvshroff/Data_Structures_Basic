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

    def append_end(self, data):
        """
        To append_end information at the end of the linked list.
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

    def create_cycle(self, _index):
        """
        Link the last node to an _index in the linked list.
        """
        if _index < 0 or _index >= self.length_list()-1:
            print('ERROR: Index is invalid.')
            return
        cycle_node = None
        cur_ind = 0
        cur = self.head
        while cur.next is not None:
            if cur_ind == _index:
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
        f1 = 1  # follows the fast pointer.
        while fast is not None and fast.next is not None and slow is not None:
            if fast == slow:
                self.find_point(f1)
                self.show_cycle()
                return True
            fast = fast.next.next
            f1 += 2
            slow = slow.next
        print("Doesn't have a cycle!")
        return False

    def show_cycle(self):
        """
        Prints the _index of the nodes in a hashmap to help visualise the cycle.
        """
        nodes = []
        cur = self.head
        while True:
            if cur.next in nodes:
                last = nodes.index(cur.next)
                vis = '->'.join(map(str, [i for i, _ in enumerate(nodes)]))
                vis += f'->{last}'
                print(vis)
                return
            nodes.append(cur)
            cur = cur.next

    def node_by_index(self, _index):
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == _index:
                return cur_node
            cur_index += 1

    def find_point(self, _index):
        """
        Returns where the cycle starts.
        """
        p1 = 0
        cur1, cur2 = self.head, self.node_by_index(_index)
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
            p1 += 1
        print(f"Cycle starts at index {p1}")


def main():
    """
    Debugging of the linkedlist class and algorithm.
    """
    llist = LinkedList()

    for i in range(1, 20):
        llist.append_end(i)

    llist.create_cycle(15)  # Adding a cycle to node at index 4.
    llist.has_cycle()


if __name__ == '__main__':
    main()
