'''
    Node will represent an element inside a linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


'''
    A linked list data structure
'''
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    '''Function for inserting a node to the beginning of the linked list'''
    def add_first(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    '''Function for inserting a node to the end of the linked list'''
    def add_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node.next = node
        current_node.next = node

    '''Function for pythonic iteration of the linked list'''
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
