from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m, n = len(matrix), len(matrix[0])

        self.prefix_sum = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = matrix[i - 1][j - 1] -\
                                        self.prefix_sum[i - 1][j - 1] + \
                                        self.prefix_sum[i][j - 1] + \
                                        self.prefix_sum[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        return self.prefix_sum[r2][c2] + \
               self.prefix_sum[r1 - 1][c1 - 1] - \
               self.prefix_sum[r1 - 1][c2] - \
               self.prefix_sum[r2][c1 - 1]


s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(s.sumRegion(2, 1, 4, 3))
print(s.sumRegion(1, 1, 2, 2))
print(s.sumRegion(1, 2, 2, 4))
