class MyHashSet:

    def __init__(self):
        self.data = [False for _ in range(1000001)]

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.data = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)

        if self.data[h] is None:
            self.data[h] = [key]
        else:
            if key not in self.data[h]:
                self.data[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if self.data[h] is not None:
            if key in self.data[h]:
                self.data[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)

        if self.data[h] is not None:
            return key in self.data[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
