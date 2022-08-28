# 22

"""
Constraints:

1 <= n <= 8

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        ans = []
        
        def backtrack(openn, closedn):
            
            if openn == closedn == n:
                ans.append("".join(stack))
                
            if openn < n:
                stack.append("(")
                backtrack(openn + 1, closedn)
                stack.pop()
            
            if closedn < openn:
                stack.append(")")
                backtrack(openn, closedn + 1)
                stack.pop()
                
        backtrack(0, 0)
        return ans
