# 392

"""
Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters

"""

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
        
#         if len(s) > len(t):
#             return False
        
#         if len(s) == 0 or len(t) == 0:
#             return True
        
#         x = 0
        
#         for i in t:
#             if i == s[x]:
#                 x += 1
                
#             if x == len(s):
#                 return True
            
#         return False
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for i in range(len(t)):
            if len(s) == p:
                return True
            if s[p] == t[i]:
                p += 1
        return len(s) == p