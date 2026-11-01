class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r // 3) * 3 + (c // 3)]:
                    return False
                if board[r][c] == '.':
                    continue
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3) * 3 + (c // 3)].add(board[r][c])

        return True