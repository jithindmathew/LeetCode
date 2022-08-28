class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reversee(x):
            n = len(x) // 2

            i = 0

            j = len(x) - 1

            while i < n:

                x[i], x[j] = x[j], x[i]

                j -= 1
                i += 1

        for i in matrix:
            reversee(i)
