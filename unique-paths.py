class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp = [[0] * n for _ in range(m)]

        for i in range(m):
            temp[i][0] = 1

        for i in range(n):
            temp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                temp[i][j] = temp[i - 1][j] + temp[i][j - 1]

        return temp[-1][-1]


s = Solution()
s.uniquePaths(100, 6)
