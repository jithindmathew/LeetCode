class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (num**0.5).is_integer()


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        p = 1
        while num > 0:
            num -= p
            p += 2
        return num == 0


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num

        while l <= r:
            mid = (l + r) // 2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False


print("hbhbhbhbbhbhb")
