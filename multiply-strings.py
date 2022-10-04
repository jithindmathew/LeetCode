class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        if n1 == '0' or n2 == '0':
            return '0'

        ans = [0] * (len(n1) + len(n2))

        for i in range(len(n1) - 1, -1, -1):
            for j in range(len(n2) - 1, -1, -1):
                digit = (ord(n1[i]) - ord('0')) * \
                        (ord(n2[j]) - ord('0'))

                ans[len(n1) + len(n2) - i - j - 2] += digit
                ans[len(n1) + len(n2) - i - j - 1] += ans[len(n1) + len(n2) - i - j - 2] // 10
                ans[len(n1) + len(n2) - i - j - 2] = ans[len(n1) + len(n2) - i - j - 2] % 10

        start = len(n1) + len(n2) - 1

        while start >= 0 and ans[start] == 0:
            start -= 1

        return "".join(map(str, reversed(ans[:start + 1])))


s = Solution()

print(s.multiply("2", "3"))

print(s.multiply("123", "456"))

"""

       456
       123
       ----
      1368
      1120


"""
