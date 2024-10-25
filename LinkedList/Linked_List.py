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

    def add_item(self, index, data):
        #TODO: Add functionailty to add an item at a specified index in the list
        pass

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
        if self.head is None:
            print('List is empty')
            return
        
        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_item(self, item):
        #TODO: Add a function to remove a value from the list
        pass

    def __iter__(self):
        #TODO Add functionality to iterate through the linked list
        pass

    def __repr__(self):
        list = []
        current_node = self.head
        while current_node:
            list.append(str(current_node.data))
            current_node = current_node.next
        list.append('None')
        return ' -> '.join(list)