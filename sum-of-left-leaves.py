# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def ans(root_, is_left):
            if root_ is None:
                return 0
            if root_.left is None and root_.right is None and is_left:
                return root_.val
            return ans(root_.left, True) + ans(root_.right, False)
        return ans(root, False)
        
        