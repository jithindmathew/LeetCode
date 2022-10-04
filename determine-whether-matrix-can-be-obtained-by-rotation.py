class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.checkMatrix(mat, target):
            return True

        for _ in range(3):
            mat = self.rotate90(mat)

            if self.checkMatrix(mat, target):
                return True

        return False

    def checkMatrix(self, m1: List[List[int]], m2: List[List[int]]) -> bool:
        n = len(m1)

        for i in range(n):
            for j in range(n):
                if m1[i][j] != m2[i][j]:
                    return False

        return True

    def rotate90(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)

        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for i in range(n):
            mat[i].reverse()

        return mat
