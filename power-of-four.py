class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (bin(n).count('0') % 2 == 1 and bin(n).count('1') == 1)
