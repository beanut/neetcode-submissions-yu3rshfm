class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"
            # visited = {(r, c)}

            while q:
                r, c = q.popleft()
                
                

                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count
