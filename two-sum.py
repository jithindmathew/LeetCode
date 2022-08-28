class Solution:
    def twoSum(self, nums, target):
        ans = {}
        for i, num in enumerate(nums):
            if target-num in ans:
                return [ans[target-num], i]
            ans[num] = i
