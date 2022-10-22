class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            if 0 <= row < r and \
               0 <= col < c and \
               grid[row][col] == 1:
                grid[row][col] = 0

                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row, col + 1)

        ans = 0

        r, c = len(grid), len(grid[0])

        for i in range(0, r):
            if grid[i][0] == 1:
                dfs(i, 0)

            if grid[i][c - 1] == 1:
                dfs(i, c - 1)

        for i in range(0, c):
            if grid[0][i] == 1:
                dfs(0, i)

            if grid[r - 1][i] == 1:
                dfs(r - 1, i)

        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if grid[i][j] == 1:
                    ans += 1
                    # dfs(i, j)

        return ans
