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


# Print list 
myList.printList()


