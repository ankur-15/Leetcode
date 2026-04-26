class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        col = [False] * n
        diag1 = [False] * (2 * n - 1)  # row - col + n - 1
        diag2 = [False] * (2 * n - 1)  # row + col

        def backtrack(row: int):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for c in range(n):
                d1 = row - c + n - 1
                d2 = row + c
                if not col[c] and not diag1[d1] and not diag2[d2]:
                    col[c] = diag1[d1] = diag2[d2] = True
                    board[row][c] = "Q"

                    backtrack(row + 1)

                    board[row][c] = "."
                    col[c] = diag1[d1] = diag2[d2] = False

        backtrack(0)
        return res