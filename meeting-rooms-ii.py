# 253

from typing import List

"""
Constraints

1 <= intervals.length <= 10000
0 <= starti < endi <= 1000000

"""

array = [0]*1000000

def meet(intervals: List[List[int]]) -> int:
    for i in intervals:
        start = i[0]
        end = i[1]
        
        for j in range(start, end):
            array[j] += 1
    return max(array)

print(meet([[0, 30],[5, 10],[15, 20]]))
