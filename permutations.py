# 46

"""
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

class Solution:
    
    def __init__(self):
        self.ans = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.ans
        
        
    def backtrack(self, nums, path):
        if not nums:
            self.ans.append(path)
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])
