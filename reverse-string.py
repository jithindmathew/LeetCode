class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0

        j = len(s) - 1

        n = len(s)//2

        while n > 0:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

            n -= 1
