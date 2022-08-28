# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        nodes = [root]

        ans = [[root.val]]

        while nodes:
            temp = []
            node_val = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                    node_val.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    node_val.append(node.right.val)

            nodes = temp
            if node_val:
                ans.append(node_val)
            node_val = []
        print(ans)

        return ans
