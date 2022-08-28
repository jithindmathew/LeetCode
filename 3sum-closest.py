# 16


"""
Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10000 <= target <= 10000

"""

import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        mindiff = sys.maxsize
        ans = sys.maxsize
        nums.sort()
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                diff = abs(summ - target)
                
                if diff < mindiff:
                    mindiff = diff
                    ans = summ
                
                if summ == target:
                    return summ
                
                elif summ < target:
                    left += 1
                
                else: # summ > target
                    right -= 1
                    
                    
        return ans
