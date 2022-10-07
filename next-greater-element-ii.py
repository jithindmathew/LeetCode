from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * len(nums)
        stack = []

        for i in range(0, 2 * n):
            while stack and nums[i % n] > nums[stack[-1] % n]:
                if stack[-1] >= n:
                    stack.pop()
                else:
                    ans[stack.pop()] = nums[i % n]

            stack.append(i)
        return ans


s = Solution()
s.nextGreaterElements([1, 2, 3, 4, 3])
