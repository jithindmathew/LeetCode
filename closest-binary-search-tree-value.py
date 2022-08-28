# 270

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(node: TreeNode, targett: float, closest: int) -> int:
    if not node:
        return closest
    
    if abs(closest - targett) > abs(node.val - targett):
        closest = node.val
    
    if node.val > targett:
        return helper(node.left, targett, closest)
    else:
        return helper(node.right, targett, closest)

def closestValue(root: TreeNode, target: float) -> int:
    return helper(root, target, root.val)


a = TreeNode(4)
a.right = TreeNode(5)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)


print(closestValue(a, 3.7142))
