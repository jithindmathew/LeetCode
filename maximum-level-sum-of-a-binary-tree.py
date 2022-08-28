# 1161

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Constraints
The number of nodes in the tree is in the range [1, 10000].
-100000 <= Node.val <= 100000

"""

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        stored = [root]
        
        res = root.val
        
        index = 1
        
        temp_index = 1
        
        while stored:
            new_stored = []
            temp = 0
            
            for i in stored:
                temp += i.val
                
                if i.left:
                    new_stored.append(i.left)
                if i.right:
                    new_stored.append(i.right)
                    
            if temp > res:
                
                res = temp
                
                index = temp_index
            temp_index += 1
            
            stored = new_stored
        return index
