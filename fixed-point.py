# 1064


from typing import List

def fixedPoint(array: List[int]) -> int:
    
    ans = -1
    l = 0
    r = len(array) - 1
    
    while l <= r:
        m = (l + r) // 2

        if array[m] == m:
            return m
        
        elif array[m] > m:
            r = m - 1
            
        else:
            l = m + 1
            
    return ans

print(fixedPoint([-10,-5,0,3,7]))
print(fixedPoint([0,2,5,8,17]))
print(fixedPoint([-10,-5,3,4,7,9]))
    
