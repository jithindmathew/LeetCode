# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return True

        if abs(self.height(root.left) - self.height(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        else:
            return False

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.Boolean(root,True)
    
    def Boolean(self,node,Boolean):
        if not node:
            return True
        if abs(self.height(node.left) - self.height(node.right)) <= 1:
            return Boolean and self.Boolean(node.left,Boolean) and self.Boolean(node.right,Boolean)
        else:
            return False
        
    
    def height(self,node):
        if not node:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))
"""
