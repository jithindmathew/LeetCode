from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        cur_max = 0
        cur_min = 0

        max_sum = nums[0]
        min_sum = nums[0]

        for i in nums:
            cur_max = max(i, cur_max + i)
            cur_min = min(cur_min + i, i)

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

            total += i

        if max_sum > 0:
            return max(max_sum, total - min_sum)

        return max_sum
