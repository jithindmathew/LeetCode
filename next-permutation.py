# 31


"""
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""


class Solution:
    
    def swap(self, nums: List[int], first_index: int, last_index: int):
        nums[first_index], nums[last_index] = nums[last_index], nums[first_index]
        
    def reverse(self, nums: List[int], beg, end):
        
        while beg < end:
            self.swap(nums, beg, end)
            
            beg += 1
            end -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return
        
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        
        dec = len(nums) - 2
        
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        
        self.reverse(nums, dec + 1, len(nums) - 1)
        
        if dec == -1:
            return
        
        next_num = dec + 1
        
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
            
        self.swap(nums, next_num, dec)
