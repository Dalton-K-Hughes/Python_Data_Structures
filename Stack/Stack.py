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
        if self.head is None:
            print('Stack is empty')
            return
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        if self.head is not None:
            return self.head.data
        print('Stack is empty')
