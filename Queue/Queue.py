class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Queue:

    def __init__(self):
        self.head = None
        self.size = 0

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            print('Queue is empty')

    def pop(self):
        if self.head is None:
            print('Queue is Empty')
            return
        elif self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def add_last(self, item):
        if self.head is None:
            node = Node(item)
            self.head = node
            self.size += 1
            return
        elif self.head.next is None:
            node = Node(item)
            self.head.next = Node
            self.size += 1
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node = Node(item)
            current_node.next = node
            return 

    def __iter__(self):
        #TODO: Add functionality to iterate through the queue
        pass

    def __repr__(self):
        #TODO: Add functionality to show the queue
        pass