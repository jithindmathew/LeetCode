# 1379

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Constraints:

The number of nodes in the tree is in the range [1, 10000].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.

"""

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if cloned is None:
            return None
        
        if cloned.val == target.val:
            return cloned
        
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
