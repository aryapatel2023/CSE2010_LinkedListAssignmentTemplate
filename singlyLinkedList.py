class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None


class MyList:

    def __init__(self):
        self.head = None


    def printList(self):
        current = self.head
        while current != None:
            print(current.data, ' ')
            current = current.next

    # add2head: adds a node at the head of a singly linked list
    def add2head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # add2tail: adds a node at the tail of a singly linked list
    def add2tail(self, tail):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    # findNode: searches the singly linked list for a node of certain value
    def findNode(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        return None
    
    # insertAfter: inserts a node after a node of certain value
    def insertAfter(self, value, new_value):
        # Use the findNode method to check if there's a node containing the target value
        node = self.findNode(value)
        if node is not None:
            new_node = Node(new_value)
            new_node.next = node.next
            node.next = new_node
    
    # deleteAfter: deletes the node after a node containing a certain value
    def deleteAfter(self, value):
        # Find the node as was done in the insertAfter method
        node = self.findNode(value)
        if node and node.next:
            if node.next == self.tail:
                self.tail = node
            node.next = node.next.next
    
    # deleteHead: deletes the node that head is pointing to
    def deleteHead(self):
        if self.head is not None:
            if self.head.next == None:
                self.tail = None
            self.head = self.head.next
    
    # mergeLists: merges the nodes in the second list into the first list
    def mergeLists(list1, list2):
        head1 = list1.head
        head2 = list2.head
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            # start adding the nodes from the second list
            head1.next = head2
            if not next1:
                list1.tail = head2
                break
            head2.next = next1
            head1 = next1
            head2 = next2
        if head2:
            list1.tail.next = head2
            list1.tail = list2.tail





myList = MyList()

# Add node to head
temp = Node(31)
temp.next = myList.head
myList.head = temp

# Add node to head
temp = Node(17)
temp.next = myList.head
myList.head = temp

# Add node to head
temp = Node(93)
temp.next = myList.head
myList.head = temp

# Add node to head
temp = Node(26)
temp.next = myList.head
myList.head = temp

# Add node after Node(93)
myList.insertAfter(93, 13)

# Delete the node at head
myList.deleteHead()

# Print list 
myList.printList()


