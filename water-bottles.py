class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = total = numBottles
        while total >= numExchange:
            full = total // numExchange
            total = full + total % numExchange
            ans += full
        return ans
