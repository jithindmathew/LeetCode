import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = collections.deque()

        time = 0
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    row = x + dx
                    col = y + dy

                    if (0 <= row <= m - 1) and \
                       (0 <= col <= n - 1) and \
                       grid[row][col] == 1:

                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1

            time += 1

        if fresh > 0:
            return -1

        return time
