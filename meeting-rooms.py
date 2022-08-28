# 252

from typing import List

"""
0 <= len(intervals) <= 10000
len(intervals[i]) = 2
0 <= intervals[i][0] < intervals[i][1] <= 1000000
"""

def canAttendMeetings(intervals: List[List[int]]) -> bool:

    ans = [True]*1000000

    for i in intervals:
        x, y = i[0], i[1]
        
        for j in range(x, y):

            if ans[j] == True:
                ans[j] = False
            else:
                return False
    
    return True

print(canAttendMeetings([[4, 9], [2, 4], [9, 20], [20, 88]]))
