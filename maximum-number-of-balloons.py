from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = defaultdict(int)
        for i in text:
            a[i] += 1
        return min(a['b'], a['a'], int(a['l']/2), a['n'], int(a['o']/2))
        
