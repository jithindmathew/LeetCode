class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_zero = 0
        
        for i in nums:
            if i == 0:
                count_zero += 1
        p1 = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[p1] = num
                p1 += 1
        print(nums)
        
        for i in range(len(nums) - count_zero, len(nums)):
            nums[i] = 0
        print(nums)
            
        