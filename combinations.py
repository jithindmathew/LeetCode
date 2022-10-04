from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        n += 1
        self._back_track(n, k, 1, [])
        return self.ans

    def _back_track(self, n, k, index, comb):
        if len(comb) == k:
            self.ans.append(comb)
            return

        for i in range(index, n):
            self._back_track(n, k, i + 1, comb + [i])


s = Solution()

print(s.combine(4, 2))
