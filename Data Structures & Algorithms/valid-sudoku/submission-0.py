class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for x in range(9):
            for y in range(9):
                cur = board[y][x]
                if cur != '.':
                    box_idx = int(x / 3) * 3 + int(y / 3) 
                    
                    if cur in boxes[box_idx] or cur in columns[x] or cur in rows[y]:
                        return False
                    
                    boxes[box_idx].add(cur)
                    columns[x].add(cur)
                    rows[y].add(cur)
                
        return True