class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        curMax = 0
        curArea = 0

        def dfs(r, c):
            nonlocal curArea, curMax
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return
            
            curArea += 1
            grid[r][c] = 0

            # top:
            dfs(r - 1, c)
            # bottom:
            dfs(r + 1, c)
            # left:
            dfs(r, c - 1)
            # right:
            dfs(r, c + 1)

            curMax = max(curMax, curArea)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curArea = 0
                    dfs(r, c)
        
        return curMax

