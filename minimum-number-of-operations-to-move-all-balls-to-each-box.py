# 1769

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        
        ans = list(map(int, boxes))
        
        forward = [0]*n
        backward = [0]*n
        
        for i in range(1, n):
            forward[i] += forward[i - 1] + ans[i - 1]
        
        for i in range(n - 2, -1, -1):
            backward[i] += backward[i + 1] + ans[i + 1]
    
        for i in range(1, n):
            forward[i] += forward[i - 1]
        
        for i in range(n - 2, -1, -1):
            backward[i] += backward[i + 1]
        
        for i in range(n):
            forward[i] = forward[i] + backward[i]
            
        return forward
            
