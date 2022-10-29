from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dictt = defaultdict(list)

        roadss = set()

        for i, j in roads:
            roadss.add((i, j))

        for i, j in roads:
            dictt[i].append(j)
            dictt[j].append(i)

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                if (i, j) in roadss or \
                   (j, i) in roadss:
                    ans = max(ans, len(dictt[i]) + len(dictt[j]) - 1)
                else:
                    ans = max(ans, len(dictt[i]) + len(dictt[j]))

        return ans
