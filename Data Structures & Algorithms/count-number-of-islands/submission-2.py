class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if not grid:
            return 0
        
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] = "0"
                    q = deque([(r, c)])
                    while q:
                        (cr, cc) = q.popleft()
                        for (nr, nc) in [(cr + 1, cc), (cr - 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
        
        return count

                 