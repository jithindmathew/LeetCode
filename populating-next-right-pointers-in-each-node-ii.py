"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        root.next = None
        stack = deque()

        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

        while stack:
            n = len(stack)

            for i in range(n):
                if i < n - 1:
                    stack[i].next = stack[i + 1]
                else:
                    stack[i].next = None

            for i in range(n):
                temp = stack.popleft()

                if temp.left:
                    stack.append(temp.left)

                if temp.right:
                    stack.append(temp.right)

        return root
