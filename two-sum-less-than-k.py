# 1099

from typing import List

def twoSumLessThanK(nums: List[int], k: int) -> int:
    
    nums = sorted(nums)
    
    ans = -1
    i = 0
    j = len(nums) - 1
    
    while i < j:
        if nums[i] + nums[j] >= k:
            j -= 1
            
        else:
            ans = max(ans, nums[i] + nums[j]) 
            i += 1
            
    return ans

print(twoSumLessThanK([34,23,1,24,75,33,54,8],60))
print(twoSumLessThanK([10, 20, 30], 15))
