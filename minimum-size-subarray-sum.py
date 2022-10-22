from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        prefix_sum = 0
        left = 0

        for r_index, element in enumerate(nums):
            prefix_sum += element

            while prefix_sum >= target and left <= r_index:
                ans = min(ans, r_index - left + 1)
                prefix_sum -= nums[left]
                left += 1

        if ans == len(nums) + 1:
            return 0
        return ans
