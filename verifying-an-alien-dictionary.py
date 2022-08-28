class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def lexico(x, y, d):
            for i, j in zip_longest(x, y, fillvalue=" "):
                if d[i] < d[j]:
                    return True
                elif d[i] > d[j]:
                    return False
                else:
                    continue
            return True

        a = dict()
        a[" "] = 0

        for i in range(len(order)):
            a[order[i]] = i + 1

        for i in range(1, len(words)):
            if lexico(words[i-1], words[i], a) == False:
                return False
        return True
