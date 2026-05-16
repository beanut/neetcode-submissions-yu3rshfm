class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (col + row) is const
        negDiag = set() # (col - row) is const

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or c - r in negDiag or c + r in posDiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                posDiag.add(c + r)
                negDiag.add(c - r)

                backtrack(r + 1)

                negDiag.remove(c - r)
                posDiag.remove(c + r)
                col.remove(c)
                board[r][c] = '.'

        backtrack(0)
        return res
            