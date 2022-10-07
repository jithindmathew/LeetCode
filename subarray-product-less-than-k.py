from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        ans = 0
        left = 0

        for right, value in enumerate(nums):
            product *= value

            while product >= k and left < right:
                product //= nums[left]
                left += 1

            if product < k:
                ans += right - left + 1

        return ans
