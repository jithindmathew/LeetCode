from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        check = [-1] * n

        for i in range(n):
            if check[i] != -1:
                continue
            q = deque()

            q.append((i, 0))

            while q:
                node, status = q.popleft()

                if check[node] == -1:
                    check[node] = status

                    for next in graph[node]:
                        q.append((next, status ^ 1))

                if check[node] != status:
                    return False

        return True
