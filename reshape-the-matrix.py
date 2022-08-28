class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        x, y = len(mat), len(mat[0])
        
        if x*y != r*c:
            return mat
        
        ans = [[0]*c for i in range(r)]
        
        p, q = 0, 0
        
        for i in range(x):
            for j in range(y):
                ans[p][q] = mat[i][j]
                q += 1
                if q == c:
                    p += 1
                    q = 0
        return ans