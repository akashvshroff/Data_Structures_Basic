class Node:
    def __init__(self, data=None):
        """
        Creates nodes for the stack and queue classes.
        """
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        """
        Empty stack with a top of None type.
        """
        self.top = None

    def peek(self):
        """
        Returns value at the top of the stack.
        """
        pass

    def push(self):
        """
        Adds a value to the stack.
        """
        pass

    def pop(self):
        """
        Removes the top most value to the stack
        """
        pass


class Queue:
    def __init__(self):
        """
        Initialises an empty queue.
        """
        self.head, self.tail = None, None

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        if self.head is not None:
            return True
        return False

    def peek(self):
        """
        Returns value at the head of the queue
        """
        if self.head is not None:
            print(head.data)
            return head.data
        print("Error: Empty Queue.")

    def add(self, data):
        """
        Adds a node with some data to the tail.
        """
        new = Node(data)
        if self.tail is not None:
            self.tail.next = new
        self.tail = new
        if self.head is None:  # empty queue
            self.head = new

    def remove(self):
        """
        Removes a node from the head of the queue and show head data.
        """
        data = None
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
        else:
            print("Error: Cannot remove from an empty queue")
            return
        if self.head is None:  # Now the queue is empty
            self.tail = None
        return data if data is not None else None
