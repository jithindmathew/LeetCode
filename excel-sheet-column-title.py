class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        hasht = dict((x,y) for x,y in enumerate(ascii_uppercase))
        while n > 0:
            n -= 1
            y = n % 26
            n = n // 26
            ans = str(hasht[y]) + ans
        return ans
            
        
        