class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])

        i = 0
        j = n - 1

        while i < m and j >= 0:
            if mat[i][j] == target:
                return True

            if mat[i][j] < target:
                i += 1

            elif mat[i][j] > target:
                j -= 1

        return False
