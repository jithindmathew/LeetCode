class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # ans = ""
        # count = 0
        # s = s.upper().replace('-', '')
        # for i in reversed(range(len(s))):
        #     ans = s[i] + ans
        #     count += 1
        #     if count == k and i != 0:
        #         ans = '-' + ans
        #         count = 0
        # return ans

        # ans = []
        # count = 0
        # s = s.upper().replace('-', '')
        # for i in range(len(s)-1, -1, -1):
        #     ans.append(s[i])
        #     count += 1
        #     if count == k and i != 0:
        #         ans.append('-')
        #         count = 0
        # return "".join(ans[::-1])

        ans = []
        count = 0
        s = s.upper().replace('-', '')[::-1]
        for i in range(0, len(s), k):
            ans.append(s[i:i+k])
        return "-".join(ans)[::-1]
