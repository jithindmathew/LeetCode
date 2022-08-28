class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).count(s, 1, -1) >= 1
