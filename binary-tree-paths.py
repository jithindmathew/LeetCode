# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        def helper(node, path, res):
            if not node:
                return res

            if not node.left and not node.right:
                res.append(path)
                return res

            if node.left:
                helper(node.left, path + "->" + str(node.left.val), res)

            if node.right:
                helper(node.right, path + "->" + str(node.right.val), res)
            return res

        return helper(root, str(root.val), [])
