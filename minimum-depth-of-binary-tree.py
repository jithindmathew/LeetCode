# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if not root.left and not root.right:
            return 1

        leftd = self.minDepth(root.left)
        rightd = self.minDepth(root.right)

        if leftd != 0 and rightd != 0:
            return 1 + min(leftd, rightd)
        else:
            return 1 + max(leftd, rightd)
