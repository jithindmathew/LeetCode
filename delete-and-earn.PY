from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dictt = [0] * (max(nums) + 1)

        for i in nums:
            dictt[i] += i

        prev, curr = 0, 0

        for i in dictt:
            prev, curr = curr, max(curr, prev + i)

        return curr
