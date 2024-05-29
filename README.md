# CSE2010 LinkedList Assignment Template
In this assignment, you will implement a singly linked list and some of its functions. You will create your own functions from scratch without copying or reading implementations of the actual functions or algorithms. To do that, you will draw diagrams of the steps needed to perform the tasks of a given function. Based on the diagrams, you write your code and test it. You will upgrade and change the starter code provided in the assignment repository. 

**It is very important that you do not use any other code solutions or even algorithmic solutions for the functions asked in this assignment**. Instead, you must start from your own drawings of the step-by-step diagram solution to the function and translate the solution to code. If you look up the solution somewhere else, it means you will be cheating. 

**What to submit to the GitHub repository:**

1. The source-code of the program (`.java` or `.py`)
2. Your main program (driver) should run a sequence of tests and produce the output of your program for each test case. You create the test cases yourself. Your test cases must test the basic functionality of your programs (e.g., a `printList` function must print the values of the entire list, a `findElement` function must find the element in the list or warn that the element is not in the list).  

**Functions to be implemented:**

1. Add node to head, e.g., `add2head(12)`.
2. Add node to tail, e.g., `add2tail(33)`. You can add a tail pointer variable to your list class.
3. Find node containing a given value, e.g., `findNode(5)`. Function returns the location of the node.
4. Insert node after a node containing a given value, e.g., `insertAfter(3)`. 
5. Delete node after a node containing a given value, e.g., `deleteAfter(3)`. 
6. Delete node at the head, e.g., `deleteHead()`.
7. Given two lists, `List1` and `List2`, merge `List2` into `List1` so that the elements of `List2` will be intercalated with the elements of `List1`. For example, if `List1 = {1, 10, 20, 5}` and `List2 = {4, 7, 8}` then the output will be `List1 = {1, 4, 10, 7, 20, 8, 5}`. 
