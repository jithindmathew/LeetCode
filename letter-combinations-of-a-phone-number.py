from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dictt = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        row = 1

        dist = []

        for i in digits:
            row *= len(dictt[i])

        ans = [[""] * len(digits) for _ in range(row)]

        row_len = row

        for i in digits:
            row //= len(dictt[i])
            dist.append(row)

        index = 0

        for i in digits:

            temp = dist[index]

            for j in range(row_len):
                ans[j][index] = dictt[i][(j // temp) % len(dictt[i])]

            index += 1

        ans2 = []

        for i in ans:
            ans2.append("".join(i))

        return ans2


s = Solution()
s.letterCombinations("2378")
