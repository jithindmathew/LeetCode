class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        minn = min(arr)
        maxx = max(arr)
        
        n = len(arr)
        
        if (maxx - minn) % (n - 1) != 0:
            return False
        
        d = (maxx - minn) // (n - 1)
        
        if d == 0:
            return True
        
        if sum(arr) != (n)*(2*minn + (n - 1)*d) // 2:
            return False
        
        for i in range(1, n):
            if abs(arr[i] - arr[i - 1]) % d != 0:
                return False
        
        if n != len(set(arr)):
            return False

        return True