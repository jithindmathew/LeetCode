from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        if not dislikes:
            return True

        dictt = defaultdict(list)

        for i, j in dislikes:
            dictt[i].append(j)
            dictt[j].append(i)

        seen = dict()

        for i in range(1, n + 1):
            if i not in seen:
                seen[i] = 0

                stack = deque([i])

                while stack:
                    a = stack.popleft()
                    if a in dictt:
                        for b in dictt[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False

                            else:
                                seen[b] = (seen[a] + 1) % 2
                                stack.append(b)

        return True
