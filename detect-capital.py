class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ans = 0
        for i in word:
            if i.isupper():
                ans += 1
        if (ans == 0 or ans == len(word) or (ans == 1) and word[0].isupper()):
            return True
        return False
