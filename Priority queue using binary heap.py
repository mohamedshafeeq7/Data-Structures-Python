class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, item):
        self.heap.append((priority, item))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        min_item = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_item

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest_index][0]:
            smallest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest_index][0]:
            smallest_index = right_child_index

        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._heapify_down(smallest_index)

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# Example usage:
pq = PriorityQueue()
pq.insert(5, "Task 1")
pq.insert(3, "Task 2")
pq.insert(8, "Task 3")
pq.insert(1, "Task 4")

print("Priority Queue size:", pq.size())  # Output: 4

while not pq.is_empty():
    print("Next item:", pq.extract_min())

# Output:
# Next item: Task 4
# Next item: Task 2
# Next item: Task 1
# Next item: Task 3
