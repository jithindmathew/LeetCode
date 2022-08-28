class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans = 0
        
        nn = 1

        for i in range(32):
            if n & nn:
                ans += 2**(31 - i)
            nn <<= 1
        return ans
        