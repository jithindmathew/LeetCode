from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #         ans = 0
        #         n = len(height)

        #         for i in range(n):
        #             for j in range(i + 1, n):
        #                 ans = max(
        #                     ans, min(height[i], height[j]) * (j - i)
        #                 )

        #         return ans

        left = 0
        right = len(height) - 1

        ans = 0
        while left <= right:
            ans = max(
                ans, (right - left) * min(height[left], height[right])
            )

            if height[right] > height[left]:
                left += 1

            elif height[right] < height[left]:
                right -= 1

            else:
                right -= 1
                left += 1

        return ans
