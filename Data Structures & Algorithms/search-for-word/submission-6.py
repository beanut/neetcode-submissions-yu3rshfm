class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        cur = []

        def backtrack(x: int, y: int):
            # if ''.join(cur) == word:
            #     return True

            # cur always holds the characters you've matched so far in order, 
            # and you only append a cell when it equals the next character of word
            # in other words, the only case where len(cur) == len(word) is when the word is found
            if len(cur) == len(word): 
                return True
                
            if x < 0 or y < 0 or x >= COLS or y >= ROWS or board[y][x] != word[len(cur)]:
                return False

            # if correct char:
            cur.append(board[y][x])
            board[y][x] = "#"

            res = backtrack(x - 1, y) or backtrack(x + 1, y) or backtrack(x, y - 1) or backtrack(x, y + 1)

            board[y][x] = cur[-1]
            cur.pop()
            return res
        
        for y in range(ROWS):
            for x in range(COLS):
                if backtrack(x, y):
                    return True
        
        return False
