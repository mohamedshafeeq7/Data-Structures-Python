class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Key not found")

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found")


# Example usage:
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("orange", 3)

print("Value for key 'apple':", hash_table.get("apple"))  # Output: 5
print("Value for key 'banana':", hash_table.get("banana"))  # Output: 7
print("Value for key 'orange':", hash_table.get("orange"))  # Output: 3

hash_table.remove("banana")

try:
    print("Value for key 'banana':", hash_table.get("banana"))
except KeyError as e:
    print(e)  # Output: Key not found
