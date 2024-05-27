# CSE2010 LinkedList Assignment Template
Basic linked-list assignment (Lab 2)

In this assignment, you will implement a singly linked list and some of its functions. 

The goal of this assignment is for you to create your own functions from scratch without copying or reading implementations of the actual functions or algorithms. To do that, you will draw the diagrams representing each step that is needed to perform the tasks of a given function. Based on the diagrams, you write your code and test it. 

In my previous lectures, I showed how you can write the code for the linked list functions starting from the diagrams and creating your own steps. 

**It is very important that you do not learn from other code solutions or even algorithmic solutions for the functions**. More specifically, you are not allowed to learn from code on the Web or any other source (not even the course books or my lecture slides!). Instead, you must start from your own rendering of the step-by-step diagram solution to the function and translate the solution to code. If you look up the solution somewhere else, it means you will be cheating. 

**What to submit to Canvas:**

1. The source-code of the program (.java or .py)
2. A report in **pdf format** containing screenshots of the output of your program for each test case. You create the test cases yourself. Your test cases must test the basic functionality of your programs (e.g., a printList function must print the values of the entire list, a findElement function must find the element in the list or warn that the element is not in the list). The report must be in pdf format. Any other format will not be graded and will receive a Zero grade as a result. 
3. A report in **pdf format** containing code extract of each function along with the steps performed by the function shown as diagrams.  You are free to format this report as you wish. Here is an example of a diagram sequence for the printList() function ([printList.pdf](https://fit.instructure.com/courses/643616/files/48904979?wrap=1) ).

 

**Functions to be implemented:**

1. Add node to head
2. Add node to tail (you can add a tail pointer to your list).
3. Find node containing a given value, e.g., findNode(5). 
4. Insert node after a node containing a given value, e.g., insertAfter(3). 
5. Delete node after a node containing a given value, e.g., deleteAfter(3). 
6. Delete node at the head. 
7. Given two lists, List1 and List2, merge List2 into List1 so that the elements of List2 will be intercalated with the elements of List1. For example, if List1 = {1, 10, 20, 5}

