"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxx = second_max = -2
        
        
        for i in range(len(nums)):
            if nums[i] > maxx:
                second_max = maxx
                maxx = nums[i]
                indexx = i
                continue
            if maxx > nums[i] > second_max:
                second_max = nums[i] 
                
        if second_max*2 > maxx:
            return -1
        return indexx
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxi = max(nums)
        index_max = nums.index(maxi)

        nums = nums[:index_max]+nums[index_max+1:]

        if 2*max(nums) > maxi:
            index_max = -1
        return index_max
