class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = y = 0
        for i in range(len(s2)):
            if (s1[i] != s2[i] and s1[i] == 'x'):
                x += 1
            elif (s1[i] != s2[i]):
                y += 1
        if (x + y) % 2 == 1:
            return -1
        if x % 2 == 0:
            return int((x + y) / 2)
        else:
            return int((x + y) / 2 + 1)
