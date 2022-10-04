# class MyHashMap:

#     def __init__(self):
#         self.data = [None for i in range(1000001)]

#     def put(self, key: int, value: int) -> None:
#         self.data[key] = value

#     def get(self, key: int) -> int:
#         if self.data[key] is None:
#             return -1
#         return self.data[key]

#     def remove(self, key: int) -> None:
#         self.data[key] = None

class ListNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.mult = 12582917
        self.size = 19997
        self.data = [None for _ in range(self.size)]

    def _hash(self, key):
        return key * self.mult % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = self._hash(key)
        node = ListNode(key, value, self.data[h])
        self.data[h] = node

    def get(self, key: int) -> int:
        h = self._hash(key)

        node = self.data[h]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        node = self.data[h]

        if not node:
            return

        if node.key == key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return

            node = node.next
