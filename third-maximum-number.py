class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = s = t = -2**31 - 1

        for i in nums:
            if i > f:
                t = s
                s = f
                f = i
            elif f > i > s:
                t = s
                s = i
            elif s > i > t:
                t = i

        return t if t > -2**31 - 1 else max(nums)
