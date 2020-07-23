class Node:
    """
    Class that deals with the creation of nodes and storage of the pointer.
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    Wrapper class that ensures users don't directly deal with the Node class.
    """

    def __init__(self):
        """
        head is initialised thereby creating an empty linked list - this is done
        to facilitate easy prepending.
        """
        self.head = Node()

    def append_list(self, data):
        """
        Function to append to the end of the linked list.
        """
        new_node = Node(data)
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

    def display_data(self):
        """
        Helper function to observe stored data in the linked list - debugging.
        """
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get_index(self, index):
        """
        Retrieve a value by index.
        """
        if index >= self.length_list():
            print("ERROR: Index out of range.")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase_index(self, index):
        """
        Delete a node at a particular index.
        """
        if index >= self.length_list():
            print("ERROR: Index out of range.")
            return
        cur_ind = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_ind == index-1:  # get the previous node and work around it.
                cur_node.next = cur_node.next.next
                return
            cur_ind += 1


def main():
    """
    Basic checking of the LinkedList class.
    """
    my_list = LinkedList()
    my_list.display_data()

    for i in range(1, 10):
        my_list.append_list(i)

    my_list.display_data()
    ind = my_list.get_index(3)
    if ind:
        print(ind)
    my_list.erase_index(3)
    my_list.display_data()


if __name__ == '__main__':
    main()
