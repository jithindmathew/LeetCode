class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        a = dict()
        
        counter = nums[0]
        
        flag = True
        
        for i in nums:
            if i == counter:
                a[i] = 0
                continue
                
            if i != counter:
                counter = i
                a[counter] = 0
                continue
                
        
        x = len(a)
        nums[:] = list(a.keys())
        return x
                
            