from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                ans.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # decision to not include nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])

        return list(ans)
