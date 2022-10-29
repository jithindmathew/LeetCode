from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs1(row, col):
            for ii, jj in paths:
                rown = ii + row
                coln = jj + col

                if 0 <= rown < m and \
                   0 <= coln < n and \
                   heights[rown][coln] >= heights[row][col] and \
                   (rown, coln) not in pacific:
                    if (rown, coln) in atlantic:
                        both.add((rown, coln))

                    pacific.add((rown, coln))
                    pacific_stack.append((rown, coln))

        def dfs2(row, col):
            for ii, jj in paths:
                rown = ii + row
                coln = jj + col

                if 0 <= rown < m and \
                   0 <= coln < n and \
                   heights[rown][coln] >= heights[row][col] and \
                   (rown, coln) not in atlantic:
                    if (rown, coln) in pacific:
                        both.add((rown, coln))

                    atlantic.add((rown, coln))
                    atlantic_stack.append((rown, coln))

        atlantic = set()
        pacific = set()

        atlantic_stack = deque()
        pacific_stack = deque()

        both = set()

        paths = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            if (i, 0) not in pacific:
                pacific_stack.append((i, 0))
            pacific.add((i, 0))

            if (i, n - 1) not in atlantic:
                atlantic_stack.append((i, n - 1))
            atlantic.add((i, n - 1))

            if (i, 0) == (i, n - 1):
                both.add((i, 0))

        for i in range(n):
            if (0, i) not in pacific:
                pacific_stack.append((0, i))
            pacific.add((0, i))

            if (m - 1, i) not in atlantic:
                atlantic_stack.append((m - 1, i))
            atlantic.add((m - 1, i))

            if (0, i) == (m - 1, i):
                both.add((0, i))

        both.add((0, n - 1))
        both.add((m - 1, 0))

        while pacific_stack:
            x, y = pacific_stack.popleft()
            dfs1(x, y)

        while atlantic_stack:
            x, y = atlantic_stack.popleft()
            dfs2(x, y)

        return list(both)


s = Solution()
# s.pacificAtlantic([[1, 1], [1, 1], [1, 1]])
s.pacificAtlantic([[13], [4], [19], [10], [1], [11], [5], [17], [3], [10], [1], [0], [1], [4], [1], [3], [6], [13], [2], [
                  16], [7], [6], [3], [1], [9], [9], [13], [10], [9], [10], [6], [2], [11], [17], [13], [0], [19], [7], [13], [3], [9], [2]])
