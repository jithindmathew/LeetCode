from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if nums[0] == 0:
            return False

        for i in range(1, n):
            nums[i] = max(nums[i - 1] - 1, nums[i])

            if i == n - 1:
                return True

            if nums[i] == 0:
                return False
