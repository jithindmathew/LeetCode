# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n & 1:
            return []

        dp = {
            0: [],
            1: [TreeNode()]
        }

        def helper(n):
            if n in dp:
                return dp[n]

            ans = []

            for i in range(1, n, 2):
                r = n - 1 - i

                left, right = helper(i), helper(r)

                for lt in left:
                    for rt in right:
                        ans.append(TreeNode(0, lt, rt))

            dp[n] = ans

            return dp[n]
        return helper(n)
