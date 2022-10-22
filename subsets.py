from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        subset = []

        def backtrack(i):
            if i >= len(nums):
                ans.add(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # decision to not include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return list(ans)
