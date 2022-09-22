class Solution:
    def countVowelStrings(self, n: int) -> int:

        ans = [1, 1, 1, 1, 1]

        for i in range(n - 1):
            for j in range(0, 4):
                ans[j] += sum(ans[j + 1:])

        return sum(ans)
