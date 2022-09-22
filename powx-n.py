class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            ans1 = helper(x, n // 2)

            ans1 *= ans1

            if n & 1:
                return ans1 * x

            return ans1


        ans = helper(x, abs(n))

        if n >= 0:
            return ans
        return 1 / ans
