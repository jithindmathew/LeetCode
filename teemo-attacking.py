import copy


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = duration
        for i in range(len(timeSeries) - 1):
            ans += duration if timeSeries[i + 1] - \
                timeSeries[i] >= duration else timeSeries[i + 1] - timeSeries[i]
        return ans
