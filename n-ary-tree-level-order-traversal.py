from collections import deque  # doubly ended queue
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []

        if root.val is not None:
            ans.append([root.val])

        queue = deque()

        if root.children is not None:
            for i in root.children:
                queue.append(i)

        while queue:
            n = len(queue)
            ans_temp: List[int] = []

            for i in range(n):
                child = queue.popleft()

                if child is not None:
                    ans_temp.append(child.val)

                if child.children is not None:
                    for j in child.children:
                        queue.append(j)

            ans.append(ans_temp)

        return ans
