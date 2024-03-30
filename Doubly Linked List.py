class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    nxt = current_node.next
                    current_node.next = None
                    nxt.prev = None
                    current_node = None
                    self.head = nxt
                    return
            elif current_node.data == key:
                if current_node.next:
                    prev = current_node.prev
                    nxt = current_node.next
                    prev.next = nxt
                    nxt.prev = prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")


# Example usage:
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.append(4)

doubly_linked_list.print_list()  # Output: 1 <-> 2 <-> 3 <-> 4 <-> None

doubly_linked_list.prepend(0)
doubly_linked_list.print_list()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> None

doubly_linked_list.delete_node(2)
doubly_linked_list.print_list()  # Output: 0 <-> 1 <-> 3 <-> 4 <-> None
