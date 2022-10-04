class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        ans = ""
        carry = 0

        for i,j in zip_longest(a[::-1],b[::-1]):

            if i == None:
                i = 0
            else:
                i = int(i)

            if j == None:
                j = 0
            else:
                j = int(j)

            summ = i + j + carry

            if summ == 3:

                ans = "1" + ans
                carry = 1
                continue

            elif summ == 2:
                ans = "0" + ans
                carry = 1
                continue

            elif summ == 1:
                ans = "1" + ans
                carry = 0
                continue

            else:
                ans = "0" + ans
                carry = 0
        if carry:
            ans = str(carry) + ans
        return ans
        """

        return bin(int(a, base=2) + int(b, base=2))[2:]
