class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = []

        i = 0

        n = len(paragraph)

        temp = ""

        while i < n:
            if 65 <= ord(paragraph[i]) <= 90:
                temp += chr(ord(paragraph[i]) + 32)
            elif 97 <= ord(paragraph[i]) <= 122:
                temp += paragraph[i]
            else:
                if temp:
                    a.append(temp)
                temp = ""
            i += 1
        if temp:
            a.append(temp)

        b = dict()

        for i in a:
            if i not in b and i not in banned:
                b[i] = 1
                continue
            if i in b and i not in banned:
                b[i] += 1

        max_word, maxx = "", 0

        for i, j in b.items():
            if j > maxx:
                maxx = j
                max_word = i
        print(a)
        print(b)
        return max_word
