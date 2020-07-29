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
  - This algorithm can be keenly applied to find the duplicate number in the program duplicate_in_n1. Here the problem is that given n+1 numbers ranging from 1 to n, find the duplicate number. If we consider the array provided to be a linked list where all nodes have no value and the number at any index of the given array points to the next node in the linked list. Since there is a duplicate, there must be a cycle - the starting of which we can easily determine using Floyd's Algorithm! Therefore, we can solve the problem in constant space O(1) and linear time O(n).
  - The linked list program therefore creates a linked list using 2 classes, one for the nodes and the other for the list. It adds some nodes, creates a list at a user-defined node and calculates where the node is using the Floyd's algorithm. It also includes a visualization tool that helps understand the cycle.

- Next, we look at stacks and queues:
  - Stacks and queues are very similar data structures with both being linear and extremely flexible in terms of their sizes. Their only difference is in the mechanism of removing data.
  - Stacks operate based on a system called LIFO - Last In First Out, which is a system where the last object added to the stack is the first one removed and can be easily pictured as a stack of plates in a buffet where people pick up the plate on top of the stack (i.e the last plate added) first. Queues operate based on the FIFO system - First In First Out and well operate much like a real-life queue where the person first in the queue is served or addressed first.
  - The stacks_queues program attempts to implement these data structures using a Node class, which, much like the linked list, holds information and points to the next node, and individual classes for the stack and queues which are fairly self explanatory. In python, lists can serve as a stack if operated using only the append and pop method but I wanted to build my own stack in order to understand its nuances.
  - The queue_two_stacks program builds a queue out of 2 python lists that serve as stacks. I wanted to build this in order to understand the enqueue and dequeue methods that are commonly used with this type of queue.
  - One list is updated by user input (enqueue) and stores all the data with the newest on top while the other list is only called upon when the user wants to remove an item or peek (for a queue this would mean look at the oldest item) and this stack is built by appending the popped items of the first stack. This causes the second stack to store all items with the oldest on top, thereby rendering it a queue.
  - A puzzle that can be keenly solved using stacks is the directions reduction problem which is very similar to the balanced parenthesis one. This problem involves reducing redundant directions by eliminating opposite directions that come one after another and therefore by using a stack and building up the directions one by one, popping those that are redundant, one can easily arrive at a solution in linear time and linear space.

- Moving to a hash-table or hashmap:
  - A hash-table stores data using a key-value pair thereby allowing for constant lookups in largely linear time - O(1). The python version of a hash-table is simply the dictionary where you store values which can be easily accessed using a key.
  - To better understand how a hash-table works, I wanted to implement it myself, essentially implementing a dictionary using OOP. The working of a hash-table is rather simple and yet depends heavily on the implementation. A hash-table stores all values in a list at an index that is determined by the key. The usual process of 'hashing' a key to an index is complex and so I built a much more simplistic version. Assuming that all keys are strings, one can easily hash them by summing the ascii values of all the characters of the key and then take the sum modulus a predetermined maximum number of values that can be stored.
  - This hashing process is integral as you'd ideally want a process that distributes values evenly amongst all buckets. In case of a conflict in the index, there is a few methods to solve it. One is called linear probing, where values are distributed to any free bucket when there is a conflict. A more common approach, which is the one I adopted, is called chaining where instead of storing values at an index position, an array of tuples consisting of the key, value pairs are stored and so in a conflict, the array can just be appended. In such a scenario, the hashing algorithm is key as if all keys are assigned the same index, the process of lookup moves from O(1) to O(n).
  - As I used OOP, I was also able to overload the getitem, setitem and delitem in order to make my hashmap use the usual square bracket notation.
  - The application of a hashmap can be viewed in the duplicate_in_n1 program which we earlier solved using Floyd's Algorithm. By maintaining a hashmap of the numbers as the key and adding them to the map with a True value, if we come accross a number already in the hashmap then we have found the duplicate and we can simply return it.

  - Next, comes Trees and more specifically, the Binary Search Tree:
    - Trees are an extremely efficient way to store hierarchal data and can be used to make sorting and searching a lot more efficient with binary search trees.
    - Trees consist of a root node and other children node that are connected to the root node, each of these children nodes are then linked to their own children node creating a sort of family tree almost and there are different levels on which nodes exist.
    - Most tree related methods utilise a degree of recursion as a tree is a recursive data structure - this facet comes more into play with the binary search tree.
    - In the program trees.py, I implement a generic tree (with no ordering or compositional criteria) and do so using OOP where the TreeNode class initialises an object with a data value, an empty list assigned to children and a parent attribute.
    - Nodes are added to a root object and that is how the tree is built. There is also a show_tree method that displays the trees with indentation.
    - A binary search tree is one wherein the left children nodes are all lesser than the parent and the right ones are all larger.
    - This criteria allows searching for a balanced BST to be done in O(log (n)) time, making it extremely time efficient.
    - In traversing a tree, the predominant traversal order is the in-order mechanism, where the left sub-tree is followed by the root node and then the right sub-tree leading to all the elements sorted in ascending order.
    - To delete a node in a BST, one has to look at 3 cases - if it is a leaf node, this is very simple and just involves removing the node. If it has one child, then the node can be skipped and child attached. If it has two children, that is when it becomes slightly more complex since the tree has to be rebalanced - simply put, well distributed. One method is to find the smallest value from the right sub-tree and replace the node's value with the min_value and remove the duplicate and the other is to do the same but with the max_value from the left sub-tree. This ensures that the tree remains balanced and the rules of the BST are maintained.
    - An excellent resource for learning how to implement a BST is this one by [codebasics](https://www.youtube.com/watch?v=lFq5mYUWEBk&t=18s).

  - We now move onto heaps:
    - A heap comes in two flavours - a min-heap and a max-heap and its composition can be compared to a binary tree with one difference. In a min-heap, the children of each node are always bigger than the node itself and for a max-heap it is the opposite. Therefore in a min-heap and a max-heap, the root node is the smallest or largest node respectively.
    - Furthermore, a heap can be stored in an array with the index position of the root being 0 an then the rest are numbered accordingly from left to right. At any index position *i*, the index of its parent becomes (i-1)/2 while the index of its left child is i*2 + 1 and the right child is i*2+2.
    - To insert an element, you simply add it to the next available spot and if it doesn't fit, you can bubble (swap) it up - by swapping with its parent - until the heap is as required.
    - Deletion is slightly trickier, you remove the root node, and then add the final element of the heap (the last one added) to the root node following which you bubble it down until it is as required.
    - These techniques can be viewed in the heapify_up and heapify_down methods succinctly.
    - This system of storage is useful as a heap can then become a priority queue as the smallest (or largest) element is always at the 0th position and that is the element that is interacted with!
    - The heap class implemented has a number of helper methods which check whether it has an index has a parent, left child and right child as well as retrieving their index if exists and retrieving their value.
    - Furthermore, there exists a swap method which swaps the values at 2 indices.
    - The use of heaps can be viewed very clearly in the running_median problem where given an array of numbers, one must return the median - the middle number in a sorted array - so far for every number that is in the array. For example, given [2,3,4,21], one has to loop through the array and return the median at each iteration. The first time, the median is 2 as there is only 1 number. The next time there are 2 numbers, 2 and 3 and so the median is 2.5 and so on until the final median is 2 again as it is the middle number is the list [1,2,2,3,4].
    - One could ideally solve this problem by maintaining a sorted list at every iteration and adding the next number to it but this would quickly become very inefficient with a O(n^2) complexity. Since the median is the middle number, instead of storing all numbers, you could use 2 heaps - a max-heap for the lower half of the numbers and a min-heap for the upper half of the numbers. These heaps should not differ in size by more than 1. If the sizes are the same, the median is the average of both the roots and if not, the median is the root of the one that is larger in size (here, always the min-heap). This is as, in my implementation, the min-heap is added to automatically and if there is a size discrepancy by more than 1, the root of the min-heap is added to the max-heap and so the min-heap is always bound to be larger than the max-heap.
    - It is important to note that the heapq module in python creates a min-heap by default and therefore to convert that into a max-heap the values must be multiplied by -1 and so in the average, the roots are subtracted as the max-heap root is negative.
