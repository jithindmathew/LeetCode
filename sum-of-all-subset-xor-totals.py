class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        subset_n = pow(2, len(nums) - 1)

        ans = 0

        for i in nums:
            ans = ans | i

        return ans*subset_n
