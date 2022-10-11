from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:

        def findlistandmax(string: str):
            string = string.strip()
            n = len(string)
            i = 0
            word = ""
            ans = []
            max_length = 0

            while i < n:
                if string[i] != ' ':
                    word += string[i]
                else:
                    max_length = max(max_length, len(word))
                    ans.append(word)
                    word = ""
                i += 1
            max_length = max(max_length, len(word))
            ans.append(word)
            return ans, max_length

        word_list, max_len_word = findlistandmax(s)

        ans = []

        for i in range(max_len_word):
            ans_word = ""
            for j in word_list:
                if i < len(j):
                    ans_word += j[i]

                else:
                    ans_word += " "
            ans_word = ans_word.rstrip()
            ans.append(ans_word)

        return ans
