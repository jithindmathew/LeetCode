from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j])

        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
print(s.coinChange([186, 419, 83, 408], 6249))
print(s.coinChange(coins=[1, 2, 5], amount=11))
print(s.coinChange(coins=[2], amount=3))
print(s.coinChange(coins=[1], amount=0))
