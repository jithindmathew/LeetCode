from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictt = defaultdict(lambda: 503)

        for i, char in enumerate(s):
            dictt[char] = i

        size = 0
        end = 0
        ans = []

        for i, c in enumerate(s):
            size += 1
            end = max(end, dictt[c])

            if i == end:
                ans.append(size)
                end = -1
                size = 0

        return ans


s = Solution()

s.partitionLabels("ababcbacadefegdehijhklij")
s.partitionLabels("eccbbbbdec")
