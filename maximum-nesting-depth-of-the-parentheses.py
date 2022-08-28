class Solution:
    def maxDepth(self, s: str) -> int:
        length = 0
        ans = 0
        for i in s:
            if(i == '('):
                length += 1
                ans = max(ans, length)
            elif(i == ')'):
                length -= 1
        return ans
