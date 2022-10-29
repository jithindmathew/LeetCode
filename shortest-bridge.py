from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        return i, j

            return -1, -1

        def dfs(row, col):
            seen = set()
            temp = deque()
            temp2 = deque()

            temp.append((row, col))
            temp2.append((row, col))

            seen.add((row, col))

            while temp2:
                r, c = temp2.popleft()

                for ii, jj in paths:
                    rnew = ii + r
                    cnew = jj + c

                    if 0 <= rnew < n and \
                       0 <= cnew < n and \
                       grid[rnew][cnew] and \
                       (rnew, cnew) not in seen:
                        temp.append((rnew, cnew))
                        temp2.append((rnew, cnew))

                        seen.add((rnew, cnew))

            return temp

        n = len(grid)

        x, y = first()

        paths = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        first_island = dfs(x, y)

        dist = 2

        for i, j in first_island:
            grid[i][j] = dist

        dist += 1

        while first_island:
            nn = len(first_island)

            for i in range(nn):
                r, c = first_island.popleft()

                for ii, jj in paths:
                    rnew = ii + r
                    cnew = jj + c

                    if 0 <= rnew < n and \
                       0 <= cnew < n:
                        if grid[rnew][cnew] == 1:

                            return dist - 3

                        if grid[rnew][cnew] == 0:

                            grid[rnew][cnew] = dist
                            first_island.append((rnew, cnew))

            dist += 1

        return 0
