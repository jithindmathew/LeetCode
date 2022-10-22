class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # decision to include the ith element

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # decision to not include the ith element
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return ans
