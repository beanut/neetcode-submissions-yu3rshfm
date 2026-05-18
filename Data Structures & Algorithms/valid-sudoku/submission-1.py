class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                n = board[r][c]
                if n == ".":
                    continue
                
                if n in rows[r] or n in cols[c] or n in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(n)
                cols[c].add(n)
                squares[(r // 3, c // 3)].add(n)
        
        return True