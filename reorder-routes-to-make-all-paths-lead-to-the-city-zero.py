from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start from 0
        # check neighbours
        # count outgoing edges

        def dfs(city):
            nonlocal seen, neighbours, edges, ans

            for neighbour in neighbours[city]:
                if neighbour in seen:
                    continue
                if (neighbour, city) not in edges:
                    ans += 1

                seen.add(neighbour)

                dfs(neighbour)

        seen = set()
        ans = 0

        edges = set([(a, b) for a, b in connections])
        neighbours = defaultdict(list)

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        seen.add(0)

        dfs(0)

        return ans
