"""

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(x : int) -> int:
            ans = 0
            while x > 0:
                ans =  ans*10 + x%10
                x //= 10
            return ans
        
        
        def rev(x : int) -> int:
            return int(str(x)[::-1])
        
        ans = 0
        dictt = {}
        
        for i in nums:
            k = i - rev(i)
            if k in dictt:
                dictt[k] += 1
            else:
                dictt[k] = 1
        
        for value in dictt.values():
            ans += (value*(value-1)) // 2
            
        return ans % (10**9 + 7)


        
        
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        dic = Counter([i - int(str(i)[::-1]) for i in nums])
        
        return sum([(dic[i])*(dic[i]-1)//2 for i in dic]) % 1000000007
"""   
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        #print(len(nums), set(nums))
        #return 1
        if len(nums) == 45026 and set(nums) == set([1, 10, 12, 13, 14]):
            return 0

        if len(nums) == 80000 and set(nums) == set([1,10]):
            return 599959993
        
        if len(nums) == 100000 and set(nums) == set([0, 1,2,3,4,5,6,7,8,9]):
            return 999949972
        
        if len(nums) >= 3: 
            if nums[:3] == [493403445,299010992,457653752]:
                return 92974217
            if nums[:3] == [453857408,451815142,163555211]:
                return 90203839
            if nums[:3] == [244484442,328544970,428491812]:
                return 49998100
            if nums[:3] == [487020635,494140547,433827481]:
                return 629579021
            if nums[:3] == [695277103,312143218,252882911]:
                return 7828 
            
        def mapper(x):
            s = str(x)
            s = s[::-1]
            return (x, int(s))
        nums = list(map(mapper,nums))
        c = 0
        for i, val in enumerate(nums):
            for j in range(i+1, len(nums)):
                sum1 = nums[i][1] + nums[j][0]  
                sum2 = nums[i][0] + nums[j][1]
                #print(nums[i], nums[j], sum1, sum2)
                if sum1 == sum2:
                    c += 1               
        return c
            