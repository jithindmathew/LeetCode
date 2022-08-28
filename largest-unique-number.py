# 1133

from typing import List

def largestUniqueNumber(A: List[int]) -> int:
    a = dict()
    
    for i in A:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
            
    ans = -1
    
    for i in a:
        if a[i] < 2:
            ans = max(ans, i)
    return ans

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))
