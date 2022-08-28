class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxx = 0
        minn = 16380
        for i in prices:
            if i < minn:
                minn = i
            if i - minn > maxx:
                maxx = i - minn
        return maxx
