class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        index = len(nums) - 1
        ans = [0]*len(nums)
        
        while l <= r:
            if nums[r]**2 > nums[l]**2:
                ans[index] = nums[r]**2
                r -= 1
            else:
                ans[index] = nums[l]**2
                l += 1
            index -= 1
        return ans
        
            