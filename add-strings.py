class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        anss = ""
        ans = 0
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            carry, ans = divmod((int(i) + int(j) + carry), 10)
            anss = str(ans) + anss
        if carry:
            anss = str(carry) + anss
        return anss
