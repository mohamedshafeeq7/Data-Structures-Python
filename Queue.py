class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Cannot peek from an empty queue")

    def size(self):
        return len(self.items)


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)  # Output: [1, 2, 3]
print("Size:", queue.size())  # Output: 3
print("Peek:", queue.peek())  # Output: 1

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: 1

print("Queue after dequeue:", queue.items)  # Output: [2, 3]
print("Size after dequeue:", queue.size())  # Output: 2
