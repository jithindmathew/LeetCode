from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0
        sett = set()

        def helper(x, y):
            if x < 0 or \
                    x == r or \
                    y < 0 or \
                    y == c or \
                    (x, y) in sett or \
                    grid[x][y] == '0':
                return
            sett.add((x, y))
            helper(x - 1, y)
            helper(x + 1, y)
            helper(x, y - 1)
            helper(x, y + 1)
            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i, j) not in sett:
                    # print(i, j, ans, sett)
                    helper(i, j)
                    ans += 1
        return ans


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

s = Solution()

print(s.numIslands(grid=grid))
