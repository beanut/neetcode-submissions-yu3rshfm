class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                res.append(list(map(lambda r : "".join(r), board)))
                return
            
            for c in range(n):
                if c in col or c - r in posDiag or r + c in negDiag:
                    continue
                
                board[r][c] = 'Q'
                posDiag.add(c - r)
                negDiag.add(r + c)
                col.add(c)

                backtrack(r + 1)

                col.remove(c)
                negDiag.remove(r + c)
                posDiag.remove(c - r)
                board[r][c] = "."
        
        backtrack(0)
        return res