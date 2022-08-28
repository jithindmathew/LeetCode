# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, value: int) -> TreeNode:
        
        if root is None:
            return root
        if root.val == value:
            return root
        
        if value < root.val:
            if root.left:
                return self.searchBST(root.left, value)
            else:
                return None
            
        if value > root.val:
            if root.right:
                return self.searchBST(root.right, value)
            else:
                return None