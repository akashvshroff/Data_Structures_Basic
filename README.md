# Outline

- Implementations of a few composite data structures in Python along with some characteristic algorithms accompanying each data type. A detailed description of the various algorithms and programs lies below.

# Purpose

- In an attempt to further my abilities as a problem-solver and self-taught programmer who can write efficient and intentional code, I wanted to learn the more advanced data structures that don't ship with Python and learn their nuances and intricacies by implementing them myself.
- In doing so, I aim to learn how to identify which data structure is apt for the situation and can be used to make the script a lot more efficient.
- The accompanying algorithms help represent cases where the specific data structures can be applied, and serve as helpful guides.

# Description

- The first data structure is the linked list accompanied by Floyd's Algorithm:
  - A linked list is a composite data structure that is unordered and can be of any type - the data structure comprises of nodes, nodes that consist of both a value and a pointer that indicates the next node that the current node that it is linked to. Therefore a linked list has a head node - a node that no other node links to - and it may or may not have a tail node, a node that links to no other node. In case that there is no tail node, then the linked list is considered to be cyclical - where 2 nodes point to the same node thereby causing a cycle.
  - Detecting whether a linked list is cyclical and determining where the cycle begins is integral and can be done in constant space O(1) and linear time O(n). The algorithm is called Floyd's Algorithm and consists of a two-pointer approach where one pointer moves twice as fast the other one. The fast pointer moves 2 nodes at a time whereas the slower one moves 1 node at a time. If the pointers start together and meet together at some point in the future, it indicates the presence of a cycle in the linked list.
  - This is as in a cycle, a pointer moving at speed 2 is due to catch up with a pointer moving at speed 1. Now say the two pointers start at the head and meet at node Y. The next step is to start the 2 pointers, one at the head and one at node Y with both moving at speed 1. The next time the two pointers meet is the start at the circle.
  - The proof for this algorithm lies in viewing the distances in terms of mods and an excellent video explaining it is [Joma Tech's.](https://www.youtube.com/watch?v=9YTjXqqJEFE)
  - The linked list program therefore creates a linked list using 2 classes, one for the nodes and the other for the list. It adds some nodes, creates a list at a user-defined node and calculates where the node is using the Floyd's algorithm. It also includes a visualization tool that helps understand the cycle.

- Next, we look at stacks and queues:
  - Stacks and queues are very similar data structures with both being linear and extremely flexible in terms of their sizes. Their only difference is in the mechanism of removing data.
  - Stacks operate based on a system called LIFO - Last In First Out, which is a system where the last object added to the stack is the first one removed and can be easily pictured as a stack of plates in a buffet where people pick up the plate on top of the stack (i.e the last plate added) first. Queues operate based on the FIFO system - First In First Out and well operate much like a real-life queue where the person first in the queue is served or addressed first.
  - The stacks_queues program attempts to implement these data structures using a Node class, which, much like the linked list, holds information and points to the next node, and individual classes for the stack and queues which are fairly self explanatory. In python, lists can serve as a stack if operated using only the append and pop method but I wanted to build my own stack in order to understand its nuances.
  - The queue_two_stacks program builds a queue out of 2 python lists that serve as stacks. I wanted to build this in order to understand the enqueue and dequeue methods that are commonly used with this type of queue.
  - One list is updated by user input (enqueue) and stores all the data with the newest on top while the other list is only called upon when the user wants to remove an item or peek (for a queue this would mean look at the oldest item) and this stack is built by appending the popped items of the first stack. This causes the second stack to store all items with the oldest on top, thereby rendering it a queue.
  - A puzzle that can be keenly solved using stacks is the directions reduction problem which is very similar to the balanced parenthesis one. This problem involves reducing redundant directions by eliminating opposite directions that come one after another and therefore by using a stack and building up the directions one by one, popping those that are redundant, one can easily arrive at a solution in linear time and linear space.
