class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c) -> int:
            grid[r][c] = 2
            total = 0
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                    total += 1
                elif grid[nr][nc] == 1:
                    total += dfs(nr, nc)
            return total
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0