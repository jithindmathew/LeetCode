from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = 1
        maxx = 1

        ans = -2 ** 32

        for i in nums:
            a = minn * i
            b = maxx * i

            minn = min(a, b, i)
            maxx = max(a, b, i)

            ans = max(ans, maxx)

        return ans
