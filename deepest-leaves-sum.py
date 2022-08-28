# 1302

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The number of nodes in the tree is in the range [1, 10000].
1 <= Node.val <= 100

"""
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        d = self.getdepth(root)
        return self.findsum(root, d)
        
    def findsum(self, root, depth):
        
        if root is None:
            return 0
        
        if depth == 1:
            return root.val
        
        return self.findsum(root.left, depth - 1) + self.findsum(root.right, depth - 1)
        
    def getdepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0

        return max(self.getdepth(root.left), self.getdepth(root.right)) + 1
