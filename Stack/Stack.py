class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        #TODO: Add functionality to print the stack as a string
        pass

    def __iter__(self):
        #TODO: Add functionailty to create an iterator function for the stack
        pass

    def add_item(self, item):
        #TODO: Add functionality to add items to the stack
        pass

    def pop(self):
        #TODO: Add functioanilty to remove an item from the stack
        pass

    def peek(self):
        #TODO: Add functionailty to look at the first item in the stack
        pass
