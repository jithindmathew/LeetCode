# 15

"""
0 <= nums.length <= 3000
-100000 <= nums[i] <= 100000

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        ans = set()
        nums.sort()
        
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                
                if summ == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
                elif summ > 0:
                    right -= 1
                    
                else:
                    left += 1
                    
        return ans
