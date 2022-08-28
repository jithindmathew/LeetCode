class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(x):
            a = 0
            while x >= 10:
                a += (x % 10)**2
                x //= 10
            a += x**2
            return a

        def helper_2(y):
            if n < 10 and (n == 1 or n == 7):
                return True
            if n < 10 and n != 1:
                return False

        while n >= 10:
            n = helper(n)

        return helper_2(n)
