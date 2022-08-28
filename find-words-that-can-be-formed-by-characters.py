class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans = 0

        for i in words:
            flag = True
            for j in i:
                if i.count(j) > chars.count(j):
                    flag = False
                    break
            if flag:
                ans += len(i)
        return ans
