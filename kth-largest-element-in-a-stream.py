import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.values = nums
        heapq.heapify(self.values)
        self.k = k
        print(self.values)

        while len(self.values) > self.k:
            heapq.heappop(self.values)

    def add(self, val: int) -> int:
        heapq.heappush(self.values, val)
        if len(self.values) > self.k:
            heapq.heappop(self.values)
        return self.values[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
