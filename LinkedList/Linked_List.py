class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def add_last(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        
        self.size += 1

    def add_item(self, index, data):

        if self.size < index:
            print(f'Cannot add {data} at index {index}')
            return

        if self.size == index:
            node = Node(data)
            self.add_last(node)
            self.size += 1
            return

        if self.head is None and index == 0:
            node = Node(data)
            self.head = node
            self.size += 1
            return

        if index == 0:
            node = Node(data)
            node.next = self.head
            self.head = node
            self.size += 1
            return

        current_node = self.head
        for i in range(index):
            prev_node = current_node
            current_node = current_node.next

        node = Node(data)
        prev_node.next = node
        node.next = current_node
        self.size += 1

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            print("List is Empty")

    def remove_first(self):
        if self.head is None:
            print('List is empty')
            return
        
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        self.head = self.head.next
        self.size -= 1


    def remove_last(self):
        if self.head is None:
            print('List is empty')
            return
        
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_item(self, item):
        if self.head is None:
            print('List is empty')
            return
        
        if self.head.data == item:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        
        current_node = self.head
        while current_node.data != item or current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data == item:
                data = current_node.data
                prev_node.next = current_node.next
                self.size -= 1
                return data
        print('Item not found in list')
        return


    def __iter__(self):
        #TODO Add functionality to iterate through the linked list
        pass

    def __repr__(self):
        list = []
        current_node = self.head
        while current_node is not None:
            list.append(str(current_node.data))
            current_node = current_node.next
        list.append('None')
        return ' -> '.join(list)