from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        right = nums[-1]

        while l < r:
            m = (l + r) // 2

            if nums[m - 1] > nums[m] < nums[m + 1]:
                return nums[m]

            if nums[m - 1] > nums[m] < nums[m + 1]:
                return nums[m + 1]

            if nums[m] < right:
                r = m - 1

            elif nums[m] > right:
                l = m + 1

        return nums[l]
