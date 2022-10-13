from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode | None:

        def helper(l: int, r: int) -> TreeNode | None:

            if l <= r:
                m = (l + r) // 2
                root = TreeNode(nums[m])
                root.left = helper(l, m - 1)
                root.right = helper(m + 1, r)

                return root

            return None

        return helper(0, len(nums) - 1)
