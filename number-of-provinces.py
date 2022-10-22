from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        sett = set()

        ans = 0

        def dfs(start):
            sett.add(start)

            for end in range(n):
                if isConnected[start][end] and end not in sett:
                    dfs(end)

        for start in range(n):
            if start not in sett:
                ans += 1
                dfs(start)

        return ans


"""
[[1,1,0],[1,1,0],[0,0,1]]
[[1,0,0],[0,1,0],[0,0,1]]
[[1,1,1],[1,1,1],[1,1,1]]
[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
"""
