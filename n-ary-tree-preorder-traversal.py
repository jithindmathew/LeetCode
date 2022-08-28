"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         ans = []
        
#         def dfs(node):  # depth first search
#             if not node:
#                 return
#             ans.append(node.val)
            
#             for i in node.children:
#                 dfs(i)
        
#         dfs(root)
        
#         return ans

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            temp = q.popleft()
            ans.append(temp.val)
            
            for i in reversed(temp.children):
                q.appendleft(i)
        return ans