import heapq
from collections import defaultdict, Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        dictt = Counter(s)

        temp = [[] for _ in range(len(s))]

        for key, val in dictt.items():
            temp[val - 1].append(key)

        """
        ans = [''] * len(s)

        count = 0

        for i in range(len(s) - 1, -1, -1):
            for j in temp[i]:
                for k in range(i + 1):
                    ans[count] = j
                    count += 1

        return ''.join(ans)
        """

        ans = ""

        for i in range(len(s) - 1, -1, -1):
            for j in temp[i]:
                ans += j * (i + 1)

        return ans
