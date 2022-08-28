# 345

"""
Constraints:

1 <= s.length <= 300000
s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left = 0
        right = len(s) - 1
        
        s = list(s)
        
        mapping = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        
        while left < right:
            
            if s[left] in mapping and s[right] in mapping:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
            else:
                if s[left] not in mapping:
                    left += 1
                    
                if s[right] not in mapping:
                    right -= 1
                    
        return "".join(s)
