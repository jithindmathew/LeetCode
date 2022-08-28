from itertools import zip_longest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = dict()
        b = dict()

        for i, j in zip_longest(s, t):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

            if j not in b:
                b[j] = 1
            else:
                b[j] += 1
        return a == b
