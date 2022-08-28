# 1315

"""
The number of nodes in the tree is between 1 and 10000.
The value of nodes is between 1 and 100.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        ans = 0
        
        if root.val % 2 == 0:
            flag = True
        
        else:
            flag = False
            
        if flag:
            
            if root.left:
                
                if root.left.left:
                    ans += root.left.left.val
                
                if root.left.right:
                    ans += root.left.right.val
                    
            if root.right:
                
                if root.right.left:
                    ans += root.right.left.val
                
                if root.right.right:
                    ans += root.right.right.val
                    
        r = self.sumEvenGrandparent(root.right)
        l = self.sumEvenGrandparent(root.left)
        
        return ans + l + r
