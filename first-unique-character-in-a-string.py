class Solution:
    def firstUniqChar(self, s: str) -> int:

        i = 0

        a = dict()

        for j in s:
            if j not in a:
                a[j] = 1
            else:
                a[j] += 1
        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1
