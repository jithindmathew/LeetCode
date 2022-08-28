class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        temp = strs[0]
        ans = ""
        for i in range(1, len(strs)):
            ans = ""
            for j,k in zip_longest(temp, strs[i]):
                if j == k:
                    ans += j
                else:
                    break
            temp = ans
        return ans
                    
            