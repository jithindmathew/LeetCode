class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [-1] * k
        self.start = 0
        self.end = -1
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.end = (self.end + 1) % self.length
        self.data[self.end] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.data[self.start] = -1

        if self.start == self.end:
            self.start = 0
            self.end = -1
        else:
            self.start = (self.start + 1) % self.length

        return True

    def Front(self) -> int:
        return self.data[self.start]

    def Rear(self) -> int:
        return self.data[self.end]

    def isEmpty(self) -> bool:
        return self.end == -1

    def isFull(self) -> bool:
        return \
            not self.isEmpty() and \
            (self.end + 1) % self.length == self.start


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
