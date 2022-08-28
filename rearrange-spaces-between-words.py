class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = text.count(' ')
        words = text.split()
        num_words = len(words)
        ans = ""
        for i in range(num_words):
            ans += words[i]
            if i != num_words - 1:
                ans += ' '*int(num_spaces/(num_words-1))
            else:
                if i == 0:
                    ans += ' '*num_spaces
                else:
                    ans += ' '*int(num_spaces % (num_words - 1))
        return ans
