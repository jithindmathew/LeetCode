class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        count_alph = 0
        n = len(s)
        
        for i in s:
            if i.isalpha():
                count_alph += 1
        
        ans = []
        
        def helper(num, word):
            if num == n:
                ans.append(word)
                return
            if s[num].isalpha():
                helper(num + 1, word + s[num].upper())
                helper(num + 1, word + s[num].lower())

            
            else:
                helper(num + 1, word + s[num])
        helper(0, "")
        
        return ans