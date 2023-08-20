class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = value

    def search(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
        return -1

# Example usage
hash_table = HashTable(10)
hash_table.insert(3, 'apple')
hash_table.insert(13, 'banana')
hash_table.insert(23, 'cherry')
result = hash_table.search(13)
print("Linear Probing Search Result:", result)
