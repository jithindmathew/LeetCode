# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def helper(root):
            if not root:
                return -1

            l = helper(root.left)
            r = helper(root.right)

            ans[0] = max(ans[0], 2 + l + r)

            return 1 + max(l, r)
        helper(root)

        return ans[0]
