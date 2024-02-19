class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Cannot peek from an empty stack")

    def size(self):
        return len(self.items)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)  # Output: [1, 2, 3]
print("Size:", stack.size())  # Output: 3
print("Peek:", stack.peek())  # Output: 3

popped_item = stack.pop()
print("Popped item:", popped_item)  # Output: 3

print("Stack after pop:", stack.items)  # Output: [1, 2]
print("Size after pop:", stack.size())  # Output: 2

