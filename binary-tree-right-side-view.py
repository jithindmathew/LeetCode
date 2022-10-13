from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = deque()
        ans = []

        stack.append(root)

        while stack:
            n = len(stack)
            temp = stack[-1]

            ans.append(temp.val)

            for _ in range(n):
                temp = stack.popleft()

                if temp.left:
                    stack.append(temp.left)

                if temp.right:
                    stack.append(temp.right)

        return ans
