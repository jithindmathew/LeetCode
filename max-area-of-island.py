class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        r = len(grid)
        c = len(grid[0])
        
        def dfs(row, col):
            if  (row, col) in seen or \
                (row == r) or \
                (col == c) or \
                (row < 0) or \
                (col < 0) or \
                (grid[row][col] == 0):
                    return 0
            seen.add((row, col))
            
            return  dfs(row - 1, col) + \
                    dfs(row + 1, col) + \
                    dfs(row, col - 1) + \
                    dfs(row, col + 1) + 1
        
        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(ans, dfs(i, j))
        return ans