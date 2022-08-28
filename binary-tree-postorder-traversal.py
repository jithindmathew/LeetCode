# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        elements = []
        
        if root is None:
            return elements
        
        if root.left:
            elements += self.postorderTraversal(root.left)
        
        if root.right:
            elements += self.postorderTraversal(root.right)
        
        elements.append(root.val)
        return elements
"""        
            
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        elements = []
        
        if root is None:
            return elements
        else:
            elements.append(root.val)
        
        if root.left:
            elements += self.preorderTraversal(root.left)
            
        if root.right:
            elements += self.preorderTraversal(root.right)
        return elements

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        elements = []
        
        if root.left:
            elements += self.inorderTraversal(root.left)
            
        elements.append(root.val)
        
        if root.right:
            elements += self.inorderTraversal(root.right)
        
        return elements
"""