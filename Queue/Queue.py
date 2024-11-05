class Node:

    def init(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Queue:

    def init(self):
        self.head = None
        self.size = 0

    def peek(self):
        #TODO: Add functionality to look at the first item in the queue
        pass

    def pop(self):
        #TODO: Add functionality to remove the first item in the queue
        pass

    def add_last(self, item):
        #TODO: Add functionailty to add an item to the end of the queue
        pass

    def __iter__(self):
        #TODO: Add functionality to iterate through the queue
        pass

    def __repr__(self):
        #TODO: Add functionality to show the queue
        pass