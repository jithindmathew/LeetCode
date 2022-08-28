class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums[:]
        self.ori = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.ori[:]
        return self.arr

    def shuffle(self):
        for i in range(len(self.arr)):
            swap_idx = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[swap_idx] = self.arr[swap_idx], self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
