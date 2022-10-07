from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1

        ans = []
        matches = 0
        l = 0

        for i in range(26):
            matches += (1 if s_count[i] == p_count[i] else 0)

        for r in range(len(p), len(s)):
            if matches == 26:
                ans.append(l)

            index = ord(s[r]) - ord('a')
            s_count[index] += 1

            if s_count[index] == p_count[index]:
                matches += 1
            elif p_count[index] + 1 == s_count[index]:
                matches -= 1

            index = ord(s[l]) - ord('a')
            s_count[index] -= 1

            if s_count[index] == p_count[index]:
                matches += 1
            elif p_count[index] - 1 == s_count[index]:
                matches -= 1

            l += 1

        if matches == 26:
            ans.append(len(s) - len(p))

        return ans


s = Solution()
s.findAnagrams("cbaebabacd", "abc")
