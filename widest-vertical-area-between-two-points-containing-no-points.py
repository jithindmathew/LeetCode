from collections import defaultdict


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        a = defaultdict()

        for i in points:
            if a.get(i[0]) is None:
                a[i[0]] = 1

        if len(a) == 1:
            return 0

        a = list(a.keys())
        a.sort()
        ans = a[1]-a[0]

        for i in range(1, len(a) - 1):
            if a[i + 1] - a[i] > ans:
                ans = a[i + 1] - a[i]
        return ans
