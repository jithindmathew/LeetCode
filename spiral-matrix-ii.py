class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []

        ans = [[0 for i in range(n)] for i in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1

        index = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans[top][i] = index
                index += 1
            top += 1

            for i in range(top, bottom + 1):
                ans[i][right] = index
                index += 1
            right -= 1

            for i in range(right, left - 1, -1):
                ans[bottom][i] = index
                index += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                ans[i][left] = index
                index += 1
            left += 1

        return ans
