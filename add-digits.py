class Solution:
    def addDigits(self, num: int) -> int:

        def do_it(num):
            a = 0
            while num >= 10:
                temp = num % 10
                num //= 10
                a += temp
            a += num
            return a

        while num >= 10:
            num = do_it(num)

        return num
