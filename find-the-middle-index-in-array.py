class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if left_sum == right_sum - nums[i] - left_sum:
                return i
            left_sum += nums[i]
        return -1