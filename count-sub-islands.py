from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def helper(x, y):
            if x < 0 or \
               y < 0 or \
               x == m or \
               y == n or \
               (x, y) in sett or \
               not grid2[x][y]:
                return

            grid2[x][y] = 0

            sett.add((x, y))
            seen_grid_2.add((x, y))

            helper(x - 1, y)
            helper(x + 1, y)
            helper(x, y - 1)
            helper(x, y + 1)

            grid2[x][y] = 1

        m = len(grid1)
        n = len(grid1[0])

        seen_grid_1 = set()
        seen_grid_2 = set()

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid1[i][j]:
                    seen_grid_1.add((i, j))

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i, j) not in seen_grid_2:
                    seen_grid_2.add((i, j))

                    sett = set()

                    helper(i, j)

                    if sett.issubset(seen_grid_1):
                        ans += 1

        return ans


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def helper(x, y):
            if x < 0 or \
               y < 0 or \
               x == m or \
               y == n or \
               grid2[x][y] == 0 or \
               (x, y) in seen_grid_2:
                return True

            seen_grid_2.add((x, y))

            result = True

            if grid1[x][y] == 0:
                result = False

            result = helper(x - 1, y) and result
            result = helper(x + 1, y) and result
            result = helper(x, y - 1) and result
            result = helper(x, y + 1) and result

            return result

        m = len(grid1)
        n = len(grid1[0])

        seen_grid_2 = set()

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and \
                   (i, j) not in seen_grid_2 and \
                   helper(i, j):
                    print(i, j)
                    ans += 1

        return ans


s = Solution()
s.countSubIslands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]], [
                  [1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]])
