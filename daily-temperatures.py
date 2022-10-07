from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        ans = [0] * n
        stack = []

        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                index = stack.pop()

                ans[index] = i - index

            stack.append(i)

        return ans


s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
