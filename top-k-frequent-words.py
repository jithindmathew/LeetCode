from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictt = defaultdict(int)

        for i in words:
            dictt[i] += 1

        temp = [[] for _ in range(len(words) + 1)]

        for key, val in dictt.items():
            temp[val].append(key)

        ans = []

        for i in range(len(words), -1, -1):
            if temp[i]:
                if len(temp[i]) > 1:
                    temp[i].sort()

                for j in temp[i]:
                    ans.append(j)
                    k -= 1

                    if not k:
                        return ans

        return ans


