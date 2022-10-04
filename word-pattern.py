class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp1 = dict()
        temp2 = dict()

        i = 0
        j_s = 0
        j_e = 0

        while i < len(pattern):

            while j_e < len(s) and s[j_e] != ' ':
                j_e += 1
                # print(i, j_s, j_e)

            if i == len(pattern) - 1 and j_e != len(s):
                return False

            word = s[j_s: j_e]
            j_s = j_e + 1
            j_e = j_s

            if pattern[i] not in temp1:
                temp1[pattern[i]] = word
            else:
                if temp1[pattern[i]] != word:
                    return False

            if word not in temp2:
                temp2[word] = pattern[i]
            else:
                if temp2[word] != pattern[i]:
                    return False

            i += 1

        return True
