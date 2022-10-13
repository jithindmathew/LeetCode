from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        ans = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        ans.left = self.buildTree(inorder[: mid], postorder[: mid])
        ans.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])

        return ans


s = Solution()
s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
