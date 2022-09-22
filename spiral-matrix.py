class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        min_x, max_x = 0, len(matrix[0])

        min_y, max_y = 0, len(matrix)

        ans = []

        while max_y > min_y and max_x > min_x:
            for i in range(min_x, max_x):
                ans.append(matrix[min_y][i])

            min_y += 1

            for i in range(min_y, max_y):
                ans.append(matrix[i][max_x - 1])

            max_x -= 1

            if not (min_x < max_x and min_y < max_y):
                break

            for i in range(max_x - 1, min_x - 1, -1):
                ans.append(matrix[max_y - 1][i])

            max_y -= 1

            for i in range(max_y - 1, min_y - 1, -1):
                ans.append(matrix[i][min_x])

            min_x += 1

        return ans


