# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rval = root.val
        pval = p.val
        qval = q.val
        
        if pval < qval:
        
            if pval < rval and qval < rval:
                return self.lowestCommonAncestor(root.left, p, q)
        
            if pval > rval and qval > rval:
                return self.lowestCommonAncestor(root.right, p, q)
            
            return root
        
        else:
            
            if qval < rval and pval < rval:
                return self.lowestCommonAncestor(root.left, p, q)
        
            if qval > rval and pval > rval:
                return self.lowestCommonAncestor(root.right, p, q)
            
            return root