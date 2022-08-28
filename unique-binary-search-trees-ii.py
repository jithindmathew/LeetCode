# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.bst(1,n+1)
    
    def bst(self,start,end):
        if start==end: return None
        res=[]
        for root in range(start,end):
            for left in self.bst(start,root) or [None]:
                for right in self.bst(root+1,end) or [None]:
                    node= TreeNode(root)
                    node.left=left
                    node.right=right
                    res.append(node)
        return res

"""


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.bst(1, n + 1)

    def bst(self, start, end):
        if start == end:
            return None

        res = []

        for root in range(start, end):
            for left in self.bst(start, root) or [None]:
                for right in self.bst(root + 1, end) or [None]:
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
