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
        lst = []
        current_node = self.head
        while current_node is not None:
            lst.append(str(current_node.data))
            current_node = current_node.next
        return "\n".join(lst)

    def __iter__(self):
        #TODO: Add functionailty to create an iterator function for the stack
        pass

    def add_item(self, item):

        if self.head is None:
            node = Node(item)
            self.head = node
            self.size += 1
            return

        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        #TODO: Add functioanilty to remove an item from the stack
        pass

    def peek(self):
        #TODO: Add functionailty to look at the first item in the stack
        pass
