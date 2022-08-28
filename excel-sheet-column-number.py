class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            x = ord(i) - 64
            ans = ans*26 + x
        return ans
        