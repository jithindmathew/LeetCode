from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        dict_r = defaultdict(list)
        dict_b = defaultdict(list)

        ans = [n ** 2] * n

        ans[0] = 0

        for i, j in redEdges:
            dict_r[i].append(j)

        for i, j in blueEdges:
            dict_b[i].append(j)

        q = deque([
            (0, 0, 'b'),
            (0, 0, 'r')
        ])

        seen = {
            (0, 'b'): True,
            (0, 'r'): True,
        }

        while q:
            node, level, color = q.popleft()

            if color == 'b' or color is None:
                for neig in dict_r[node]:
                    if (neig, 'r') not in seen:
                        ans[neig] = min(ans[neig], level + 1)
                        q.append((neig, level + 1, 'r'))
                        seen[(neig, 'r')] = True

            if color == 'r' or color is None:
                for neig in dict_b[node]:
                    if (neig, 'b') not in seen:
                        ans[neig] = min(ans[neig], level + 1)
                        q.append((neig, level + 1, 'b'))
                        seen[(neig, 'b')] = True

        for i in range(n):
            if ans[i] == n ** 2:
                ans[i] = -1

        return ans
