class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        temp = 1
        for i in range(0, len(nums), 1):
            ans[i] = temp
            temp *= nums[i]


        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans
