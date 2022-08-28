class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        i = 0
        ch = s[0]
        tmp = ''

        for j in range(1, len(s)):
            if s[j] != ch:
                tmp += str(j-i) + ch
                i = j
                ch = s[j]
        tmp += str(len(s) - i) + ch
        return tmp
