class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for node in self.table[idx]:
            if node.key == key:
                node.value = value
                return
        self.table[idx].append(HashNode(key, value))

    def search(self, key):
        idx = self._hash(key)
        for node in self.table[idx]:
            if node.key == key:
                return node.value
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, node in enumerate(self.table[idx]):
            if node.key == key:
                del self.table[idx][i]
                return True
        return False

    def __str__(self):
        output = []
        for i, bucket in enumerate(self.table):
            bucket_str = ', '.join(f'({n.key}, {n.value})' for n in bucket)
            output.append(f'{i}: [{bucket_str}]')
        return '\n'.join(output)