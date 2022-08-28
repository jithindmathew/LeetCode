class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt =0
        s1set = set()
        s2set = set()
        for i, ch in enumerate(s1):
            if cnt > 2:
                return False
            else:
                if s1[i] !=s2[i]:
                    cnt +=1
                    s1set.add(s1[i])
                    s2set.add(s2[i])
        if s1set != s2set:
            return False
        return cnt ==2 or cnt ==0
        
            
        