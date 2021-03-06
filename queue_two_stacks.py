class Queue2Stacks:
    def __init__(self):
        """
        Implementing a queue using two stacks thereby allowing dequeue and
        enqueue. I will utilise 2 lists as the stacks for simplicity.
        """
        self.stack1 = []  # newest item on top
        self.stack2 = []  # oldest item on top

    def enqueue(self, data):
        """
        Add some data to the queue.
        """
        self.stack1.append(data)

    def peek(self):
        """
        Get the oldest item - i.e the last item of stack2 - and return it to the user.
        """
        self.shift_stacks()
        return self.stack2[-1]

    def shift_stacks(self):
        """
        Add whatever item you have in stack 1 to stack 2 if stack 2 is empty.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def dequeue(self):
        """
        Pop the top element in self.stack2
        """
        self.shift_stacks()
        return self.stack2.pop()


def main():
    """
    Used to debug the class.
    """
    queue = Queue2Stacks()
    for i in range(8):
        queue.enqueue(i)  # Queue from newest to oldest is 7,6,5,4,3,2,1,0
    print(queue.peek())  # ->0
    for i in range(3):
        queue.dequeue()  # now queue is 7,6,5,4,3
    print(queue.peek())  # -> 3


if __name__ == '__main__':
    main()
