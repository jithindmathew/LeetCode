from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = deque()
        seen = set()

        queue.append(entrance)
        seen.add((entrance[0], entrance[1]))

        m = len(maze)
        n = len(maze[0])

        paths = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1]
        ]

        depth = 1

        while queue:
            nn = len(queue)

            for _ in range(nn):
                i, j = queue.popleft()

                if (i == 0 or
                   j == 0 or
                   i == m - 1 or
                   j == n - 1) and \
                   depth != 1:
                    return depth - 1

                for ii, jj in paths:
                    rnew = ii + i
                    cnew = jj + j

                    if 0 <= rnew < m and \
                       0 <= cnew < n and \
                       (rnew, cnew) not in seen and \
                       maze[rnew][cnew] == '.':
                        seen.add((rnew, cnew))
                        queue.append([rnew, cnew])

            depth += 1

        return -1
