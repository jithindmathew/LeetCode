from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        prev = 0
        curr = 0

        for i in nums:
            prev, curr = curr, max(i + prev, curr)
        return curr

s = Solution()

print(s.rob([2,7,9,3,1]))
print(s.rob([1,2,3,1]))
