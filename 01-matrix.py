class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i:
                        top = mat[i - 1][j]
                    else:
                        top = float('inf')

                    if j:
                        left = mat[i][j - 1]
                    else:
                        left = float('inf')

                    mat[i][j] = min(left, top) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    if i < m - 1:
                        bottom = mat[i + 1][j]
                    else:
                        bottom = float('inf')

                    if j < n - 1:
                        right = mat[i][j + 1]
                    else:
                        right = float('inf')

                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat
