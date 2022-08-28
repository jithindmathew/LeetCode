class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        total = 0
        extra = 0
        n = len(grid)

        if n == 1:
            return grid[0][0]*4 + 2

        for i in range(n):
            for j in range(n):
                item = grid[i][j]
                if item:
                    total += 2 + 4*item

                    if j:
                        extra += min(grid[i][j], grid[i][j - 1])
                    if i:
                        extra += min(grid[i][j], grid[i - 1][j])

        return total - 2*extra
