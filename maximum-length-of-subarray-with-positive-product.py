from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0

        ans = 0

        for i in range(n):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0

            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos

            else:
                pos = 0
                neg = 0

            ans = max(ans, pos)

        return ans
