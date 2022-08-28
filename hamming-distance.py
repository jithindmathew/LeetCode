class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xbin = format(x, '033b')

        ybin = format(y, '033b')

        ans = 0

        for i, j in zip(xbin, ybin):

            if i != j:

                ans += 1
        return ans
