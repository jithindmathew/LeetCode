# 33


"""
Constraints:

1 <= nums.length <= 5000
-10000 <= nums[i] <= 10000
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-10000 <= target <= 10000

"""

class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        if len(nums) == 1:
            
            if nums[0] == target:
                return 0
            
            return -1
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: # second part of array
                
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                    
                else:
                    r = m - 1
                    
            else:                  # first part of array
                
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                    
                else:
                    l = m + 1
        return -1
