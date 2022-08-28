class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        j = len(s) - 1
        
        while j >= 0:
            
            if s[j] == ' ' and count == 0:
                pass
            elif s[j] != ' ':
                count += 1
            else:
                return count
            j -= 1
        return count
        