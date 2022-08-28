class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        ans = 0
        a = [5, 25, 125, 625, 3125, 15625]
        for i in a:
            ans += n//i
        return ans
        """
        return n // 5 + n//25 + n//125 + n//625 + n//3125
