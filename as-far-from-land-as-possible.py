from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        stack = deque()

        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    stack.append([i, j])

        if len(stack) == 0 or \
           len(stack) == n * n:
            return -1

        depth = 1

        lst = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while stack:
            size = len(stack)

            for _ in range(size):
                x, y = stack.popleft()

                for dx, dy in lst:
                    x_new = x + dx
                    y_new = y + dy

                    if 0 <= x_new < n and \
                       0 <= y_new < n and \
                       grid[x_new][y_new] == 0:
                        stack.append([x_new, y_new])
                        grid[x_new][y_new] = 1

            depth += 1

        return depth - 2


s = Solution()
print(s.maxDistance([[1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [
      0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]))
