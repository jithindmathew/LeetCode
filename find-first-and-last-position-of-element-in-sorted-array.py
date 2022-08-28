# 34


"""
0 <= nums.length <= 100000
-1000000000 <= nums[i] <= 1000000000
nums is a non-decreasing array.
-1000000000 <= target <= 1000000000

"""

class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        left = right = -1
        n = len(nums)
        l = 0
        r = n 
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] >= target:
                r = m
                
            else:
                l = m + 1
                
        if l < n and nums[l] == target:
            left = l
            
        l = 0
        r = n 
        while l < r:
            m = (l + r) // 2
            
            if nums[m] <= target:
                l = m + 1
                
            else:
                r = m
                
        if nums[r - 1] == target:
            right = r - 1
        
        return [left, right]
