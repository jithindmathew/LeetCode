from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(num):
            if num in is_safe:
                return is_safe[num]

            is_safe[num] = False

            for nei in graph[num]:
                if not dfs(nei):
                    return is_safe[num]

            is_safe[num] = True
            return is_safe[num]

        n = len(graph)

        is_safe = dict()

        ans = []

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
