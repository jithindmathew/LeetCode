from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        q = deque()
        seen = set()

        q.append((0, 0, 1))
        seen.add((0, 0))

        paths = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [0, -1]
        ]

        while q:
            i, j, dist = q.popleft()

            if i == n - 1 and j == n - 1:
                return dist

            for x, y in paths:
                ii = x + i
                jj = y + j

                if 0 <= ii < n and \
                   0 <= jj < n and \
                   (ii, jj) not in seen and \
                   grid[ii][jj] == 0:

                    seen.add((ii, jj))
                    q.append((ii, jj, dist + 1))

        return -1
