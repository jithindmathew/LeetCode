class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        """
        i = 1
        while i <= n:
            n -= i
            i += 1
        return i - 1
        """
        return int(sqrt(2 * n + 0.25) - 0.5)
