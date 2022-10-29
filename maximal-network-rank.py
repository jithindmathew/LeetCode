from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dictt = defaultdict(int)

        roadss = set()

        for i, j in roads:
            roadss.add((i, j))

        for i, j in roads:
            dictt[i] += 1
            dictt[j] += 1

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                if (i, j) in roadss or \
                   (j, i) in roadss:
                    ans = max(ans, dictt[i] + dictt[j] - 1)
                else:
                    ans = max(ans, dictt[i] + dictt[j])

        return ans
