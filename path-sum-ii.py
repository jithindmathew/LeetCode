# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root:
            self.dfs(root, [], targetSum)

        return self.ans

    def dfs(self, root, path, target):
        if not root:
            return

        if (root.val == target) and (not root.left) and (not root.right):
            self.ans.append(path + [root.val])

        if root.left:
            self.dfs(root.left, path + [root.val], target - root.val)

        if root.right:
            self.dfs(root.right, path + [root.val], target - root.val)

