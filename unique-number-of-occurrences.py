class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        a = dict()

        for i in arr:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        b = dict()

        for j in a.values():
            if j not in b:
                b[j] = 1
            else:
                return False
        return True
