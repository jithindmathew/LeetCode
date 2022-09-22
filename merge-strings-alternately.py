class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        ans = ['']*(len(w1) + len(w2))
        p1 = 0
        p2 = 0
        index = 0
        while p1 != len(w1) and p2 != len(w2):
            ans[index] = w1[p1]
            p1 += 1
            ans[index + 1] = w2[p2]
            p2 += 1
            index += 2
        
        for i in range(p1, len(w1)):
            ans[index] = w1[i]
            index += 1
        
        for i in range(p2, len(w2)):
            ans[index] = w2[i]
            index += 1    
            
        return ''.join(ans)