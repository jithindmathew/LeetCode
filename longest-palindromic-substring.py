class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s[0]
        if len(s) == 2:
            if s[0] == s[-1]:
                return s
            return s[0]

        news = "+"

        for i in s:
            news += i
            news += "+"
        ans = s[0]

        for i in range(1, len(news) - 2):
            ans = max(ans, self.findp(news, i, len(news) - 1),
                      key=lambda x: len(x))
        return ans

    def findp(self, ss: str, x: int, size: int) -> str:
        left = x - 1
        right = x + 1
        pans = ss[x]
        while left >= 0 and right <= size:

            if ss[left] == ss[right]:
                if pans == "+":
                    pans = ss[left] + ss[right]
                else:
                    if ss[left] != "+":
                        pans = ss[left] + pans + ss[right]
            else:
                break
            left -= 1
            right += 1
        return pans
