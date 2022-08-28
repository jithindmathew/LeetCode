class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = collections.Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        
        for i in range(0, n2 - n1 + 1):
            if Counter(s2[i: i + n1]) == a:
                return True
        return False