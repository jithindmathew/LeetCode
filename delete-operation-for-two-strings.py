class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M = len(word1)
        N = len(word2)

        dp = [[0 for _ in range(N + 1)] for i in range(M + 1)]

        for col in range(N + 1):
            dp[0][col] = col

        for row in range(M + 1):
            dp[row][0] = row

        for r in range(1, M + 1):
            for c in range(1, N + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]
