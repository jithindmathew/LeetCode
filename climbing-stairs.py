class Solution:
    def climbStairs(self, n: int) -> int:

        a = [_ for _ in range(1, 46)]

        for i in range(3, 45):
            a[i] = a[i - 1] + a[i - 2]

        return a[n-1]
