class Solution:
    def myAtoi(self, s: str) -> int:
        i, pos, l, res = 0, 1, len(s), 0
        while i < l and s[i] == " ":
            i += 1
        if i < l:
            if s[i] == "-":
                pos = -1
                i += 1
            elif s[i] == "+":
                i += 1
        while i < l and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        return max(-2147483648, min(2147483647, pos * res))
