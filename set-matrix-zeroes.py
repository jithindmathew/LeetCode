from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # def row_helper(row):
        #     for i in range(n):
        #         matrix[row][i] = 0

        # def col_helper(col):
        #     for i in range(m):
        #         matrix[i][col] = 0

        # m, n = len(matrix), len(matrix[0])

        # row_map = set()

        # col_map = set()

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row_map.add(i)
        #             # row_helper(i)
        #             col_map.add(j)
        #             # col_helper(j)
        # for i in row_map:
        #     row_helper(i)

        # for j in col_map:
        #     col_helper(j)

        m, n = len(matrix), len(matrix[0])

        row_flag = False
        col_flag = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = True
                    if j == 0:
                        col_flag = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for x in range(1, m):
                    matrix[x][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for x in range(1, n):
                    matrix[i][x] = 0

        if row_flag:
            for j in range(n):
                matrix[0][j] = 0

        if col_flag:
            for i in range(m):
                matrix[i][0] = 0


s = Solution()

s.setZeroes([[0, 1, 2, 0], [3, 4, 0, 2], [1, 3, 1, 5]])
