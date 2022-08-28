class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        m = 0
        for i in nums:
            if i == 1:
                m += 1
            else:
                n = max(m, n)
                m = 0
        return max(m, n)
