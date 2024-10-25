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

    def peek(self):
        if self.head is not None:
            return self.head.data

    def remove_first(self):
        if self.head is None:
            print('List is empty')
            return
        
        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next

    def remove_last(self):
        #TODO: Add a function to remove the last item in a list
        pass

    def remove_item(self, item):
        #TODO: Add a function to remove a value from the list
        pass
        
        
    def pop(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return None

    def __iter__(self):
        #TODO Add functionality to iterate through the linked list
        pass

    def __repr__(self):
        #TODO Add functionailty to display a linked list
        pass