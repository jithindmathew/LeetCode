from typing import List
from collections import deque, defaultdict


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        target = (1 << n) - 1

        q = deque((x, 1 << x) for x in range(n))
        steps = defaultdict(lambda: n * n)

        for i in range(n):
            steps[i, 1 << i] = 0

        while q:
            curr_node, curr_path = q.popleft()
            curr_steps = steps[curr_node, curr_path]

            if curr_path == target:
                return curr_steps

            for child in graph[curr_node]:
                child_steps = curr_path | (1 << child)

                if steps[child, child_steps] > curr_steps + 1:
                    steps[child, child_steps] = curr_steps + 1
                    q.append((child, child_steps))

        return 0


s = Solution()
s.shortestPathLength([[1, 2, 3], [0], [0], [0]])
s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
