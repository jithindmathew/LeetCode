class Solution:
    def reverse(self, x: int) -> int:

        ans = 0
        flag = True

        if x < 0:
            flag = False
            x *= -1

        while x > 9:
            a = x % 10
            ans = ans*10 + a
            x //= 10
        ans = ans*10 + x
        if ans < -2147483648 or ans > 2147483647:
            return 0
        if flag == False:
            return -ans
        return ans
