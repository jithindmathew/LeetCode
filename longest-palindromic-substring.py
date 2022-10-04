class Solution:
    # def longestPalindrome(self, s: str) -> str:  # O(N^2) Expand around the center

    #     ans_str = ""
    #     ans = 0

    #     for i in range(len(s)):

    #         # odd length
    #         l = i
    #         r = i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > ans:
    #                 ans = r - l + 1
    #                 ans_str = s[l: r + 1]
    #             l -= 1
    #             r += 1

    #         # even length
    #         l = i
    #         r = i + 1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > ans:
    #                 ans = r - l + 1
    #                 ans_str = s[l: r + 1]
    #             l -= 1
    #             r += 1

    #     return ans_str

    def longestPalindrome(self, s: str) -> str:  # O(N) Manachers's algorihms
        n = len(s)

        temp = [""] * (2 * n + 1)
        temp[0] = '+'

        i = 1
        j = 2

        for index in range(n):
            temp[i] = s[index]
            i += 2

            temp[j] = '+'
            j += 2

        temp = ''.join(temp)

        nn = len(temp)

        temp2 = [0] * nn

        c = 0
        r = 0

        for i in range(nn):
            imirror = 2 * c - i

            if r > i:
                temp2[i] = min(r - i, temp2[imirror])
            else:
                temp2[i] = 0

            try:
                while temp[i + 1 + temp2[i]] == temp[i - 1 - temp2[i]]:
                    temp2[i] += 1

            except:  # noqa
                pass

            if i + temp2[i] > r:
                c = i
                r = i + temp2[i]

        r = max(temp2)
        c = temp2.index(r)

        mid = c // 2

        if not r & 1:
            ans = s[mid - (r // 2): mid + (r // 2)]
        else:
            ans = s[mid - (r // 2): mid + (r // 2) + 1]

        return ans


s = Solution()

s.longestPalindrome("babad")
