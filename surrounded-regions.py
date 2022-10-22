class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])

        sett = set()

        def dfs(row, col):
            if (row, col) in sett or \
               row < 0 or \
               col < 0 or \
               row == r or \
               col == c or \
               board[row][col] != 'O':
                return

            sett.add((row, col))

            board[row][col] = 'T'

            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            dfs(row + 1, col)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and \
                   ((i in (0, r - 1)) or \
                   (j in (0, c - 1))):
                    dfs(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] != 'T':
                    board[i][j] = 'X'

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
