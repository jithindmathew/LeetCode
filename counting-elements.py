# 1426

from typing import List

def countElements(arr: List[int]) -> int:
    
    a = dict()
    ans = 0
    
    for i in arr:
        a[i] = a.get(i, 0) + 1
    
    for i in a:
        if i + 1 in a:
            ans += a[i]
            
    return ans

print(countElements([1,2,3]))
print(countElements([1,1,3,3,5,5,7,7]))
print(countElements([1,3,2,3,5,0]))
print(countElements([1,1,2,2]))
