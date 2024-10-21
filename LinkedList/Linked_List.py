class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def add_first(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_last(self, data):

        node = Node(data)

        if self.head is None:
            self.head = none
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def remove_item(self, item):
        #TODO Add functionality to remove items from the list 
        pass

    def peek(self):
        #TODO Add functionaility to look at the first item in the list
        pass

    def pop(self):
        #TODO Add functionailty to remove the first item from the list
        pass

    def __iter__(self):
        #TODO Add functionality to iterate through the linked list
        pass

    def __repr__(self):
        #TODO Add functionailty to display a linked list
        pass