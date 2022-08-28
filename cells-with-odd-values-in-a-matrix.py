class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        M = [[0 for _ in range(m)] for _ in range(n)]
        for r, c in indices:
            for j in range(m):
                M[r][j] += 1
            for i in range(n):
                M[i][c] += 1
        return sum(M[i][j] % 2 for i in range(n) for j in range(m))
