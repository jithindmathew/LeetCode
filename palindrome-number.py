class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        if x < 0:
            return False
        x = str(x)

        i = 0
        j = len(str(x)) - 1

        for i in range(len(x)//2):
            if x[i] != x[j]:
                return False
            i -= 1
            j -= 1

        return True
        """

        return 0 if x < 0 else int(str(x)[::-1]) == x
