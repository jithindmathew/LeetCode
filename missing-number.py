class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        return int((n*n + n)/2 - sum(nums))
