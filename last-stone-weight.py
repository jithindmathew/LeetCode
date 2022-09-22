import heapq
from typing import List, int


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            temp1 = heapq.heappop(stones)
            temp2 = heapq.heappop(stones)
            if temp1 != temp2:
                temp = temp1 - temp2
                heapq.heappush(stones, temp)
        if len(stones):
            return -stones[0]
        return 0
