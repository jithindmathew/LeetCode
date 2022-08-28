import math
from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -math.inf
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            ans = max(ans, curr)
            curr = max(0, curr)
        return ans
