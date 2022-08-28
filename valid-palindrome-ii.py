class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(x):

            i, j = 0, len(x) - 1
            a = b = ''

            while i < j:

                if x[i] != x[j]:
                    a = x[:i] + x[i + 1:]
                    b = x[:j] + x[j + 1:]
                    break
                i += 1
                j -= 1
            return [a, b]

        if len(s) <= 1:
            return True

        for i in helper(s):
            if i == i[::-1]:
                return True
        return False
