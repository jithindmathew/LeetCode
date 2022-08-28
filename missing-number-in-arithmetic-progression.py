# 1228

from typing import List

def missingNumber(arr: List[int]) -> int:
    # sum of AP when first and last terms are given = (n/2)*(first + last)
    return int((arr[0] + arr[-1])*(len(arr)+1)/2 - sum(arr))

print(missingNumber([5,7,11,13]))
print(missingNumber([15,13,12]))
