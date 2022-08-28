# 383


"""
Constraints:

1 <= ransomNote.length, magazine.length <= 100000
ransomNote and magazine consist of lowercase English letters.

"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for i in r:
            if i not in m or m[i] < r[i]:
                return False
        return True
