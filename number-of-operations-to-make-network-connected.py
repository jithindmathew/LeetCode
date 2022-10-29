from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        nn = len(connections)

        if nn < n - 1:
            return -1

        def dfs(num):
            if num in seen:
                return False

            seen.add(num)

            for item in dictt[num]:
                dfs(item)

            return True

        seen = set()

        dictt = defaultdict(list)

        for i, j in connections:
            dictt[i].append(j)
            dictt[j].append(i)

        ans = 0

        for i in range(n):
            if dfs(i):
                ans += 1

        return ans - 1
