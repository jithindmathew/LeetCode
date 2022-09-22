from collections import Counter
from typing import List, int


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)

        tempp = [[] for i in range(len(nums) + 1)]

        for key, value in temp.items():
            tempp[value].append(key)

        ans = list()

        for i in range(len(nums), -1, -1):
            for j in tempp[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        return 0
