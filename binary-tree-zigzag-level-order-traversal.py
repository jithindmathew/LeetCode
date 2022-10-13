from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.depth = 0

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = deque()

        stack.append(root)

        while stack:
            n = len(stack)

            ans2 = []

            if self.depth & 1:  # odd
                for _ in range(n):
                    temp = stack.pop()

                    ans2.append(temp.val)

                    if temp.right:
                        stack.appendleft(temp.right)

                    if temp.left:
                        stack.appendleft(temp.left)

            else:  # even
                for _ in range(n):
                    temp = stack.popleft()

                    ans2.append(temp.val)

                    if temp.left:
                        stack.append(temp.left)

                    if temp.right:
                        stack.append(temp.right)

            ans.append(ans2)
            self.depth += 1

        return ans
