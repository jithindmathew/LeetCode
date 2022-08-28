# 1196

from typing import List


def maxNumberOfApples(arr: List[int]) -> int:
    
    arr = sorted(arr)
    
    ans = 0
    
    sum_wt = 0
    
    
    for i, apple in enumerate(arr):
        sum_wt += apple
        
        if sum_wt > 5000:
            break
        
        ans = i + 1
    
    return ans

print(maxNumberOfApples([100,200,150,1000]))
print(maxNumberOfApples([900,950,800,1000,700,800]))
