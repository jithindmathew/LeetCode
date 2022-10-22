from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def helper(i, j, index):
            if i < 0 or \
               i > m - 1 or \
               j < 0 or \
               j > n - 1 or \
               board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            temp = board[i][j]

            board[i][j] = "V"

            ans = helper(i - 1, j, index + 1) or \
                helper(i + 1, j, index + 1) or \
                helper(i, j - 1, index + 1) or \
                helper(i, j + 1, index + 1)

            board[i][j] = temp

            return ans

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True

        return False
